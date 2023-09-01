import os
import shutil


def check_file_for_library(file_path, library):
    """Check if a file contains the specified library."""
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
        content = file.read()
        return library in content


# Define the main directory and libraries
main_dir = "20_rust_library"
libraries = ["crossbeam_channel", "std::sync::mpsc"]

# Modify the library names for folder compatibility
safe_libraries = [lib.replace("::", "_") for lib in libraries]

# Create the main directory and subdirectories
if not os.path.exists(main_dir):
    os.makedirs(main_dir)

for lib in safe_libraries:
    sub_dir = os.path.join(main_dir, lib)
    if not os.path.exists(sub_dir):
        os.makedirs(sub_dir)

# Traverse the 20_rust directory and check each .rs file
for root, dirs, files in os.walk("20_rust"):
    for file in files:
        if file.endswith('.rs'):
            file_path = os.path.join(root, file)
            library_statuses = [check_file_for_library(file_path, lib) for lib in libraries]

            # If only one library is used, copy the file to the respective directory with its folder structure
            if sum(library_statuses) == 1:
                index = library_statuses.index(True)

                # Create sub-directory structure inside target library directory using the full path as prefix
                relative_path = os.path.relpath(file_path, "20_rust")
                target_path = os.path.join(main_dir, safe_libraries[index], relative_path)

                # Ensure directory exists
                target_dir = os.path.dirname(target_path)
                if not os.path.exists(target_dir):
                    os.makedirs(target_dir)

                shutil.copy(file_path, target_path)
