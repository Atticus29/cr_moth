import pandas as pd

# Load the list of filenames from tmp.txt
with open("files_that_survived_cropping_and_hand_qa.txt", "r") as f:
    valid_filenames = set(line.strip() for line in f)

# Load the multiclass classification CSV
df = pd.read_csv("multiclass_classification.csv")

# Filter the rows where 'filename' exists in tmp.txt
filtered_df = df[df["filename"].isin(valid_filenames)]

# Save the filtered DataFrame back to CSV
filtered_df.to_csv("filtered_multiclass_classification.csv", index=False)

print("Filtered multiclass classification CSV file has been created successfully!")
