import pandas as pd

# Specify the input CSV file
input_file = "combined_output.csv"  # Change this to your input CSV file
output_file = "unique_values_output.csv"  # Name of the output file

# Specify the column name to extract unique values from
target_column = "scientificName"  # Replace with the actual column name you want to target

try:
    # Read the input CSV file
    df = pd.read_csv(input_file)

    # Check if the target column exists
    if target_column not in df.columns:
        raise ValueError(f"Column '{target_column}' not found in the input file.")

    # Extract unique values from the target column
    unique_values = df[target_column].drop_duplicates().reset_index(drop=True)

    # Save the unique values to a new CSV file
    unique_values.to_csv(output_file, index=False, header=[target_column])

    print(f"Unique values from column '{target_column}' have been written to {output_file}")

except Exception as e:
    print(f"An error occurred: {e}")
