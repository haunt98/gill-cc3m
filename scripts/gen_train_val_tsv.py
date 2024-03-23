import json
import os
from tqdm import tqdm


def process_json_files(directory, output_file):
    # Check if the output file exists, and delete it if it does
    if os.path.exists(output_file):
        os.remove(output_file)

    # Create and write the column headers
    with open(output_file, "a") as out_file:
        out_file.write("caption\timage\n")

    # Iterate over all files in the specified directory
    for filename in tqdm(os.listdir(directory), desc="Parsing dataset..."):
        if filename.endswith(".json"):
            # Construct the full file path
            filepath = os.path.join(directory, filename)

            # Open and read the JSON file
            with open(filepath, "r") as file:
                try:
                    data = json.load(file)
                except json.JSONDecodeError:
                    continue

                # Check if the status field is 'success'
                if data.get("status") == "success":
                    # Extract the values of the caption and key fields
                    caption = data.get("caption", "")
                    key = data.get("key", "") + ".jpg"

                    # Write the extracted data to the output file
                    with open(output_file, "a") as out_file:
                        out_file.write(f"{caption}\t{key}\n")


# Call the function, specifying the directory and output file paths
process_json_files("output/training_01", "processed/cc3m_train.tsv")
process_json_files("output/validation_01", "processed/cc3m_val.tsv")
