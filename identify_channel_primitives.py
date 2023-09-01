import os
import re

def identify_channel_primitives(directory_path):
    # Regular expressions to identify channel primitives
    channel_primitives_patterns = {
        "send": r"\.send\(",
        "recv": r"\.recv\(",
        "try_recv": r"\.try_recv\(",
        "drop": r"drop\(",
        "iter_recv": r"\.iter\(\)\.next\("
    }

    # Results storage
    channel_primitives_results = {
        "send": [],
        "recv": [],
        "try_recv": [],
        "drop": [],
        "iter_recv": []
    }

    # Traverse the specified directory and identify channel primitives
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            if file.endswith('.rs'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()
                    for primitive, pattern in channel_primitives_patterns.items():
                        if re.search(pattern, content):
                            channel_primitives_results[primitive].append(os.path.relpath(file_path, directory_path))

    return channel_primitives_results

# Call the function and print detailed results
rust_library_extract_path = "20_rust_library"  # Your extracted path here
results = identify_channel_primitives(rust_library_extract_path)
for primitive, files in results.items():
    print(f"\n{primitive.upper()} in files:")
    for file in files:
        print(f"- {file}")

