import pandas as pd

# Load the CSV files
species_df = pd.read_csv('species_with_30_occurrences_or_more.csv')
dl_moths_df = pd.read_csv('dl_moths_matching_gbif_not_just_spiecies.csv')

# Extract the 'value' column from the first CSV
values_to_match = species_df['Value']

# Filter the rows in the second CSV where 'scientificName' matches any value in 'value'
matching_rows = dl_moths_df[dl_moths_df['scientificName'].isin(values_to_match)]

# Extract the 'Filename' column from the matching rows
target_filenames = matching_rows['Filename']

# Save the resulting filenames to a new CSV
target_filenames.to_csv('targetFilenamesForDetection.csv', index=False, header=True)

print("Matching filenames have been saved to 'targetFilenamesForDetection.csv'.")
