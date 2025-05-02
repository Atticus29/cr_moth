import json
import pandas as pd
import subprocess
import os

# Load filenames from target CSV
target_filenames = pd.read_csv('targetFilenamesForDetection.csv')['Filename']

# Base path for images
base_path = "/Users/markfisher/Desktop/cr_moth_classification/cr_images/"

# COCO structure
coco_output = {
    "info": {
        "year": "2024",
        "version": "1",
        "description": "Exported from inference results",
        "contributor": "",
        "url": "",
        "date_created": "2024-12-13T21:23:30+00:00"
    },
    "licenses": [
        {
            "id": 1,
            "url": "https://creativecommons.org/licenses/by/4.0/",
            "name": "CC BY 4.0"
        }
    ],
    "categories": [
        {
            "id": 1,
            "name": "moth",
            "supercategory": "none"
        }
    ],
    "images": [],
    "annotations": []
}

# Annotation ID counter
annotation_id = 0

# Process each filename
for idx, filename in enumerate(target_filenames):
    image_path = os.path.join(base_path, filename)

    # Run the inference command
    cmd = [
        "inference", "infer",
        "--input", image_path,
        "--model_id", "cr-moth-detector/1",
        "--api-key", "ttlsPPRxNFZfeFqEs5hA"
    ]

    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        # Extract JSON part from the command output
        print("STDOUT:", result.stdout)
        print("STDERR:", result.stderr)
        stdout_lines = result.stdout.splitlines()
        json_part = next((line for line in stdout_lines if line.startswith("{")), None)
        json_part = json_part.replace("'", '"')
        print(f"Extracted JSON part: {json_part}")


        if json_part is None:
            print(f"No JSON output for file {filename}")
            continue

        output = json.loads(json_part)

        # Add image entry
        image_entry = {
            "id": idx,
            "license": 1,
            "file_name": filename,
            "height": output["image"]["height"],
            "width": output["image"]["width"],
            "date_captured": "2025-12-13T21:23:30+00:00"
        }
        coco_output["images"].append(image_entry)

        # Add annotations
        for prediction in output["predictions"]:
            annotation_entry = {
                "id": annotation_id,
                "image_id": idx,
                "category_id": 1,  # Assuming "moth" category
                "bbox": [
                    prediction["x"] - prediction["width"] / 2,
                    prediction["y"] - prediction["height"] / 2,
                    prediction["width"],
                    prediction["height"]
                ],
                "area": prediction["width"] * prediction["height"],
                "segmentation": [],
                "iscrowd": 0
            }
            coco_output["annotations"].append(annotation_entry)
            annotation_id += 1

    except subprocess.CalledProcessError as e:
        print(f"Error processing file {filename}: {e.stderr}")

# Save to coco.json
with open('coco_output_fisher.json', 'w') as f:
    json.dump(coco_output, f, indent=4)

print("COCO JSON file has been created as 'coco_output_fisher.json'.")
