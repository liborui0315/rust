import csv
import os

def check_file_for_library(file_path, library):
    """Check if a file contains the specified library."""
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
        content = file.read()
        return library in content

root_dir = "20_rust"
libraries = ["crossbeam_channel", "std::sync::mpsc"]
all_entries = []
use_entries = []

# Traverse the directories and check each .rs file
for root, dirs, files in os.walk(root_dir):
    for file in files:
        if file.endswith('.rs'):
            file_path = os.path.join(root, file)
            library_statuses = [check_file_for_library(file_path, lib) for lib in libraries]
            all_entries.append([file_path] + library_statuses)

            # If at least one library is used, add the file to use_entries list
            if any(library_statuses):
                use_entries.append([file_path] + library_statuses)

# Write the results to the condition_all.csv file
all_csv_file = "condition_all.csv"
with open(all_csv_file, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    headers = ["File Path"] + libraries
    csvwriter.writerow(headers)
    for entry in all_entries:
        csvwriter.writerow(entry)

# Write the results to the condition_use.csv file
use_csv_file = "condition_use.csv"
with open(use_csv_file, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    headers = ["File Path"] + libraries
    csvwriter.writerow(headers)
    for entry in use_entries:
        csvwriter.writerow(entry)

print(f"Results written to {all_csv_file} and {use_csv_file}")
