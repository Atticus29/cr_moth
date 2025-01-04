import json
import os
from PIL import Image

# Paths to the JSON file and images directory
json_path = '/Users/markfisher/Downloads/CR_Moth_Detector.v1i.coco/train/_annotations.coco.json'  # Path to your COCO JSON file
image_dir = '/Users/markfisher/Downloads/CR_Moth_Detector.v1i.coco/train/'    # Directory containing the image files

# Load the JSON file
with open(json_path, 'r') as f:
    data = json.load(f)

# Create a lookup for annotations by image_id
annotations_by_image = {}
for annotation in data['annotations']:
    image_id = annotation['image_id']
    if image_id not in annotations_by_image:
        annotations_by_image[image_id] = []
    annotations_by_image[image_id].append(annotation)

# Process each image in the images list
for image_info in data['images']:
    image_id = image_info['id']
    file_name = image_info['file_name']
    image_path = os.path.join(image_dir, file_name)

    # Check if the image file exists
    if not os.path.exists(image_path):
        print(f"Image file not found: {image_path}")
        continue

    # Open the image
    with Image.open(image_path) as img:
        # Get all annotations for this image
        annotations = annotations_by_image.get(image_id, [])
        
        for idx, annotation in enumerate(annotations):
            bbox = annotation['bbox']
            x, y, width, height = map(int, bbox)

            # Crop the image based on the bbox
            cropped_img = img.crop((x, y, x + width, y + height))

            # Create the new filename
            base_name, ext = os.path.splitext(file_name)
            cropped_file_name = f"{base_name}_cropped_{idx}.jpg"
            cropped_image_path = os.path.join(image_dir, cropped_file_name)

            # Save the cropped image
            cropped_img.save(cropped_image_path)
            print(f"Cropped image saved: {cropped_image_path}")

print("Processing complete.")
