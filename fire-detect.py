# fire-detect.py

import os
import argparse
from ultralytics import YOLO
import cv2

def detect_from_images(model_path, input_dir, output_dir):
    # Load the YOLOv11 model
    model = YOLO(model_path)

    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Process each image in the input directory
    for file_name in os.listdir(input_dir):
        file_path = os.path.join(input_dir, file_name)

        # Only process image files
        if file_name.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp')):
            print(f"Processing: {file_name}")
            img = cv2.imread(file_path)

            # Run detection
            results = model(img)

            # Plot and save results
            annotated = results[0].plot()
            output_path = os.path.join(output_dir, file_name)
            cv2.imwrite(output_path, annotated)
            print(f"Saved: {output_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Fire/Object Detection from Images using YOLOv11")
    parser.add_argument("--model", required=True, help="Path to the custom YOLOv11 model (e.g., best.pt)")
    parser.add_argument("--input", required=True, help="Path to the input image directory")
    parser.add_argument("--output", default="outputs", help="Directory to save annotated images")

    args = parser.parse_args()

    detect_from_images(args.model, args.input, args.output)
