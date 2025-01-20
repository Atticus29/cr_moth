import pandas as pd

# Input CSV file
input_file = "dl_moths_matching_gbif.csv"  # Replace with the path to your CSV file

# Column containing the scientific names
column_name = "scientificName"  # Replace with the actual column name

# Number of top frequent values to display
n = 10  # Change this to your desired number of frequent values

try:
    # Read the CSV file
    df = pd.read_csv(input_file)

    # Check if the column exists
    if column_name not in df.columns:
        raise ValueError(f"Column '{column_name}' not found in the CSV file.")

    # Calculate the frequency of each scientific name
    frequency = df[column_name].value_counts()

    # Get the top n most frequent values
    top_frequent = frequency.head(n)

    # Print the results
    print(f"Top {n} most frequent values in '{column_name}':")
    print(top_frequent)

except Exception as e:
    print(f"An error occurred: {e}")
