import os
import re

def identify_channel_creations(directory_path):
    # Regular expressions to identify channel creations
    channel_patterns = {
        "bounded": r"crossbeam_channel::bounded\((\d+)\)",
        "unbounded": r"crossbeam_channel::unbounded\(\)",
        "sync_bounded": r"std::sync::mpsc::sync_channel\((\d+)\)",
        "sync_unbounded": r"std::sync::mpsc::channel\(\)"
    }

    # Results storage
    channel_creations = {
        "bounded": [],
        "unbounded": [],
        "sync_bounded": [],
        "sync_unbounded": []
    }

    # Traverse the specified directory and identify channel creations
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            if file.endswith('.rs'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()
                    for channel_type, pattern in channel_patterns.items():
                        matches = re.findall(pattern, content)
                        if matches:
                            for match in matches:
                                channel_creations[channel_type].append({
                                    "file": os.path.relpath(file_path, directory_path),
                                    "match": match
                                })

    return channel_creations

rust_library_extract_path = "C:\\Users\\17434\\PycharmProjects\\pythonProject1\\20_rust_library"

# Call the function and print detailed results
results = identify_channel_creations(rust_library_extract_path)
for channel_type, matches in results.items():
    print(f"\n{channel_type.upper()} CHANNELS:")
    for match in matches:
        print(f"File: {match['file']}, Match: {match['match']}")

