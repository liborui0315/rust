import os

# Define the root directory
root_dir = "C:\\Users\\17434\\PycharmProjects\\pythonProject1\\20"

# Open an output file
output_file = open("project_output.txt", "w")

# Recursive function to get all .rs files from a project directory
def get_rs_files(dir_path, project_name):
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
        rs_files = get_rs_files(project_path, project)
        output_file.write(f"Project: {project}\n")
        for rs_file in rs_files:
            output_file.write(rs_file + "\n")
        output_file.write("\n")

# Close the output file
output_file.close()
