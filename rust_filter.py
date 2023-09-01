import os
import shutil

# Define the root directory
root_dir = "C:\\Users\\17434\\PycharmProjects\\pythonProject1\\20"
output_root = "20_rust"

# Create output directory if it doesn't exist
if not os.path.exists(output_root):
    os.makedirs(output_root)


# Recursive function to get all .rs files from a project directory
def get_rs_files(dir_path):
    rs_files = []
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            if file.endswith('.rs'):
                rs_files.append(os.path.join(root, file))
    return rs_files


# Loop through each directory in the root directory
for project in os.listdir(root_dir):
    project_path = os.path.join(root_dir, project)
    if os.path.isdir(project_path):
        # Get all .rs files for the current project
        rs_files = get_rs_files(project_path)

        # Create a directory for this project under output_root
        project_output_dir = os.path.join(output_root, project)
        if not os.path.exists(project_output_dir):
            os.makedirs(project_output_dir)

        # Copy each .rs file to the new project directory while preserving the directory structure
        for rs_file in rs_files:
            relative_path = os.path.relpath(rs_file, project_path)
            dest_path = os.path.join(project_output_dir, relative_path)
            dest_dir = os.path.dirname(dest_path)
            if not os.path.exists(dest_dir):
                os.makedirs(dest_dir)
            shutil.copy(rs_file, dest_path)
