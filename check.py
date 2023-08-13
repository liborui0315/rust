import os


def get_rs_files(dir_path):
    """Get all .rs files from a directory."""
    rs_files = []
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            if file.endswith('.rs'):
                rs_files.append(os.path.join(root, file))
    return rs_files


root_dir = "C:\\Users\\17434\\PycharmProjects\\pythonProject1\\20"
output_root = "20_rust"

all_copied_correctly = True

for project in os.listdir(root_dir):
    project_path = os.path.join(root_dir, project)
    project_output_dir = os.path.join(output_root, project)

    original_files = get_rs_files(project_path)
    copied_files = get_rs_files(project_output_dir)

    # Check if the number of files is the same
    if len(original_files) != len(copied_files):
        print(
            f"Project {project} has a mismatch in file count: Original {len(original_files)}, Copied {len(copied_files)}")
        all_copied_correctly = False
        continue

    # Check if all files in the original directory exist in the new directory
    for file in original_files:
        relative_path = os.path.relpath(file, project_path)
        if not os.path.exists(os.path.join(project_output_dir, relative_path)):
            print(f"File {relative_path} not found in copied project {project}.")
            all_copied_correctly = False

if all_copied_correctly:
    print("All files copied correctly!")
else:
    print("There were some issues in copying the files.")
