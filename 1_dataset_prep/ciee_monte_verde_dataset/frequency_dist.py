import pandas as pd
import matplotlib.pyplot as plt

# Input CSV file
input_file = "dl_moths_matching_gbif.csv"  # Replace with the path to your CSV file

# Column containing the scientific names
column_name = "scientificName"  # Replace with the actual column name

try:
    # Read the CSV file
    df = pd.read_csv(input_file)

    # Check if the column exists
    if column_name not in df.columns:
        raise ValueError(f"Column '{column_name}' not found in the CSV file.")

    # Calculate the frequency of each scientific name
    frequency = df[column_name].value_counts()

    # Plot the histogram
    plt.figure(figsize=(10, 6))
    frequency.plot(kind='bar')
    plt.title("Frequency of Scientific Names")
    plt.xlabel("Scientific Name")
    plt.ylabel("Frequency")
    plt.xticks(rotation=45, ha="right", fontsize=10)
    plt.tight_layout()

    # Show the plot
    plt.show()

except Exception as e:
    print(f"An error occurred: {e}")
