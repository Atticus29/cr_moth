import os
import shutil
import pandas as pd

# Directories
source_dir_1 = "cr_images_pb"
source_dir_2 = "cr_images"
destination_dir = "cr_gbif_matches"

# CSV file containing the filenames to match
csv_file = "dl_moths_matching_gbif_not_just_spiecies.csv"

# Column name in the CSV file that contains the filenames
filename_column = "Filename"

# Create the destination directory if it doesn't exist
os.makedirs(destination_dir, exist_ok=True)

try:
    # Read the CSV file
    df = pd.read_csv(csv_file)

    # Get the list of filenames from the CSV
    filenames_to_match = set(df[filename_column].dropna())

    # Function to copy files
    def copy_files(source_dir):
        for filename in os.listdir(source_dir):
            if filename in filenames_to_match:
                source_path = os.path.join(source_dir, filename)
                destination_path = os.path.join(destination_dir, filename)
                shutil.copy2(source_path, destination_path)
                print(f"Copied: {filename}")

    # Copy files from both directories
    copy_files(source_dir_1)
    copy_files(source_dir_2)

    print(f"All matching files have been copied to {destination_dir}")

except Exception as e:
    print(f"An error occurred: {e}")
