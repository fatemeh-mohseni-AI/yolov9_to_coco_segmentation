import os
import json
import cv2

def convert_yolo_to_coco(yolo_annotation_dir, image_dir, output_json_path, categories):
    coco_output = {
        "images": [],
        "annotations": [],
        "categories": categories
    }

    annotation_id = 1  # COCO annotations need unique IDs
    image_id = 1

    for annotation_file in os.listdir(yolo_annotation_dir):
        if annotation_file.endswith(".txt"):
            # Get corresponding image file
            image_filename = annotation_file.replace(".txt", ".jpg")  # Change as per image format
            image_path = os.path.join(image_dir, image_filename)

            # Load image to get width and height
            image = cv2.imread(image_path)
            height, width, _ = image.shape

            # Add image to COCO
            coco_output["images"].append({
                "id": image_id,
                "file_name": image_filename,
                "width": width,
                "height": height
            })

            # Process YOLO annotations
            with open(os.path.join(yolo_annotation_dir, annotation_file), "r") as f:
                for line in f:
                    values = line.split()

                    if len(values) < 6:
                        raise ValueError("Invalid YOLOv9 segmentation format")

                    class_id = int(values[0])
                    bbox = list(map(float, values[1:5]))
                    polygon = list(map(float, values[5:]))

                    # Convert YOLO bbox (cx, cy, w, h) to COCO format (x, y, w, h)
                    x_center, y_center, bbox_width, bbox_height = bbox
                    x_min = (x_center - bbox_width / 2) * width
                    y_min = (y_center - bbox_height / 2) * height
                    bbox_coco = [x_min, y_min, bbox_width * width, bbox_height * height]

                    # Add annotation to COCO
                    coco_output["annotations"].append({
                        "id": annotation_id,
                        "image_id": image_id,
                        "category_id": class_id,
                        "bbox": bbox_coco,
                        "segmentation": [polygon],  # Polygon is a list of x1, y1, x2, y2, ..., xn, yn
                        "area": bbox_width * bbox_height * width * height,
                        "iscrowd": 0
                    })

                    annotation_id += 1

            image_id += 1

    # Save COCO annotations to JSON
    with open(output_json_path, "w") as f:
        json.dump(coco_output, f, indent=4)


if __name__ == "__main__":

    # Usage example
    categories = [
        {"id": 1, "name": "Chicken_dead"},
        {"id": 2, "name": "Chicken_healthy"},
        {"id": 3, "name": "Chicken_sick"},
        {"id": 4, "name": "class4"},
        {"id": 5, "name": "class5"}
        # and so on
    ]
    yolo_annotation_dir = "/home/fatemeh/Documents/training_datasets/september2024/labels/"
    image_dir = "/home/fatemeh/Documents/training_datasets/september2024/images/"
    output_json_path = "/home/fatemeh/Documents/training_datasets/september2024/coco_annotations.json"
    
    convert_yolo_to_coco(yolo_annotation_dir, image_dir, output_json_path, categories)



