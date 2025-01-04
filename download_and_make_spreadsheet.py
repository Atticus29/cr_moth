import os
import requests
from bs4 import BeautifulSoup
import csv

# Function to download an image
def download_image(url, folder, filename):
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        filepath = os.path.join(folder, filename)
        with open(filepath, 'wb') as file:
            for chunk in response.iter_content(1024):
                file.write(chunk)
        return filepath
    return None

output_folder = "/Users/markfisher/Desktop/cr_moth_classification/cr_images"
os.makedirs(output_folder, exist_ok=True)

# Prepare CSV file
csv_filename = "image_data.csv"
csv_headers = ["Filename", "Identifier", "ScientificName", "CommonName", "Comments"]
with open(csv_filename, "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(csv_headers)

# Define the target URL and folder for saving images
# for pageNum in range(0,359):
for pageNum in range(0,2):
    # print(pageNum)
    url = f"https://www.discoverlife.org/mp/20p?res=640&see=I_PBA/{pageNum:04}&flags=col9:"
    print(url)


    # Fetch the webpage content
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Append rows to the CSV file
    with open(csv_filename, "a", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)

        # Parse the HTML to find image entries
        for td in soup.find_all("td", valign="top"):
            img_tag = td.find("img")
            if img_tag and "src" in img_tag.attrs:
                img_src = img_tag["src"]
                img_url = f"https://www.discoverlife.org{img_src}"
                filename = os.path.basename(img_src)

                # Download the image
                download_image(img_url, output_folder, filename)

                # Extract text elements (identifier, scientific name, common name, comments)
                text_elements = td.find_all(string=True)
                text_values = [text.strip() for text in text_elements if text.strip()]

                # Ensure exactly 4 columns (fill with None if missing)
                while len(text_values) < 4:
                    text_values.append(None)

                # Write to CSV
                writer.writerow([filename] + text_values[:4])
    print(f"Processed page {pageNum:04}: Images downloaded and data appended to '{csv_filename}'.")

print(f"Images downloaded to '{output_folder}' and metadata saved to '{csv_filename}'.")
