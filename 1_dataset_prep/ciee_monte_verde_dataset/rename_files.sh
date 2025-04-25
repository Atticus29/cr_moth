#!/bin/bash

# Loop through all files in the current directory
for file in *; do
    # Use parameter expansion to remove the pattern '_cropped_foo' where foo is any digit
    new_name=$(echo "$file" | sed -E 's/_cropped_[0-9]+//g')

    # Rename only if the new name is different from the original
    if [[ "$file" != "$new_name" ]]; then
        mv "$file" "$new_name"
        echo "Renamed: $file -> $new_name"
    fi
done

echo "Renaming complete."
