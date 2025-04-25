import os
import pandas as pd

# Specify the directory containing the CSV files
input_directory = "/Users/markfisher/Desktop/cr_moth_classification/target_csvs"  # Change this to the path where your CSV files are stored
output_file = "combined_output.csv"  # Name of the output file

# Get a list of all CSV files in the directory
csv_files = [file for file in os.listdir(input_directory) if file.endswith('.csv')]

# Combine the CSV files
combined_df = pd.DataFrame()
for csv_file in csv_files:
    file_path = os.path.join(input_directory, csv_file)
    df = pd.read_csv(file_path)
    combined_df = pd.concat([combined_df, df], ignore_index=True)

# Save the combined data to a new CSV file
combined_df.to_csv(output_file, index=False)

print(f"Combined {len(csv_files)} files into {output_file}")
