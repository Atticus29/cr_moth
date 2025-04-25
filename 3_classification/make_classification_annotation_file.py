import pandas as pd

# Load species list
species_df = pd.read_csv("species_with_30_occurrences_or_more.csv")
species_list = species_df["Value"].unique()

# Load filename-to-species mapping
moth_data = pd.read_csv("dl_moths_matching_gbif_not_just_spiecies.csv")

# Initialize an empty DataFrame with filename and species columns
columns = ["filename"] + list(species_list)
output_df = pd.DataFrame(columns=columns)

# Process each filename and species match
file_species_map = {}

for _, row in moth_data.iterrows():
    scientific_name = row["scientificName"]
    filename = row["Filename"]

    if scientific_name in species_list:
        if filename not in file_species_map:
            file_species_map[filename] = {species: 0 for species in species_list}
        
        file_species_map[filename][scientific_name] = 1  # Mark species presence

# Convert the dictionary into a DataFrame
output_data = []
for filename, species_flags in file_species_map.items():
    row = {"filename": filename}
    row.update(species_flags)
    output_data.append(row)

output_df = pd.DataFrame(output_data)

# Save to CSV
output_df.to_csv("multiclass_classification.csv", index=False)

print("Multiclass classification CSV file has been created successfully!")
