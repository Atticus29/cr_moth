import pandas as pd

# Input files
gbif_taxa = "unique_values_output_gbif_unmatched_excluded_moth_removed.csv"
dl_moths_all = "combined_output_moth_removed.csv"

# Output files
# good_matching_gbif_taxa = "good_matching_gbif_taxa.csv"
# dl_moths_matching_gbif = "dl_moths_matching_gbif.csv"
good_matching_gbif_taxa = "good_matching_gbif_taxa_not_just_species.csv"
dl_moths_matching_gbif = "dl_moths_matching_gbif_not_just_spiecies.csv"

# Step 1: Filter 1.csv for matchType == "EXACT" and rank == "SPECIES"
try:
    # Read 1.csv
    df1 = pd.read_csv(gbif_taxa)

    # Filter rows where matchType is "EXACT" and rank is "SPECIES"
    # filtered_df1 = df1[(df1["matchType"] == "EXACT") & (df1["rank"] == "SPECIES")]
    filtered_df1 = df1[(df1["matchType"] == "EXACT") ]

    # Get unique verbatimScientificName values
    unique_scientific_names = filtered_df1["verbatimScientificName"].drop_duplicates()

    # Save to a.csv
    unique_scientific_names.to_csv(good_matching_gbif_taxa, index=False, header=["verbatimScientificName"])

    print(f"Filtered scientific names written to {good_matching_gbif_taxa}")

    # Step 2: Match scientificName values from 2.csv with values in a.csv
    # Read 2.csv
    df2 = pd.read_csv(dl_moths_all)

    # Filter rows where scientificName is in the list from a.csv
    matching_df2 = df2[df2["scientificName"].isin(unique_scientific_names)]

    # Select filename and scientificName columns
    result_df2 = matching_df2[["Filename", "scientificName"]]

    # Save to b.csv
    result_df2.to_csv(dl_moths_matching_gbif, index=False)

    print(f"Matching entries written to {dl_moths_matching_gbif}")

except Exception as e:
    print(f"An error occurred: {e}")
