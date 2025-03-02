import csv
import json
import subprocess

# Input and output CSV filenames
baseDir = '/Users/markfisher/Desktop/cr_moth_classification/ready_for_classification_model/'
input_csv = "filtered_multiclass_classification.csv"  # Change to your actual file name
output_csv = baseDir + "classification_results.csv"

# API URL
api_url = "https://classify.roboflow.com/cr-moths/5?api_key=TODOttlsPPRxNFZfeFqEs5hA"

# Read the CSV and process each image
with open(baseDir+input_csv, newline='') as csvfile:
    reader = csv.reader(csvfile)
    header = next(reader)  # Get the header row
    print(header)
    
    # Add new columns for predicted class and confidence
    header.extend(["Predicted class", "Confidence"])
    
    rows = []
    
    for row in reader:
        filename = baseDir+row[0]
        print(f"filename is {filename}")
        try:
            # Encode the image and send request
            cmd = f'base64 -i "{filename}" | curl -d @- "{api_url}"'
            result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
            print(f"Result is {result}")
            
            # Parse the response
            response_json = json.loads(result.stdout)
            print(f"response_json is {response_json}")
            predictions = response_json.get("predictions", {})
            print(f"predictions is {predictions}")
            predicted_classes = response_json.get("predicted_classes", [])
            print(f"predicted_classes is {predicted_classes}")
            
            if predicted_classes:
                top_class = predicted_classes[0]
                print(f"top_class is {top_class}")
                confidence = predictions.get(top_class, {}).get("confidence", None)
                print(f"confidence is {confidence}")
            else:
                top_class = "N/A"
                confidence = "N/A"
            
            row.extend([top_class, confidence])
        except Exception as e:
            row.extend(["Error", str(e)])
        
        rows.append(row)

# Write the updated data to a new CSV
with open(output_csv, "w", newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(header)
    writer.writerows(rows)

print(f"Processing complete. Results saved to {output_csv}")