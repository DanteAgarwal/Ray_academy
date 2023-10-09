import os


def rename_directories_in_path(path):
    chapter_number = 1  # Initialize chapter number

    # Traverse all subdirectories in the given path
    for root, dirs, _ in os.walk(path):
        for directory_name in dirs:
            # Construct the full directory path
            directory_path = os.path.join(root, directory_name)

            # Split the directory name and perform renaming
            parts = directory_name.split('-')
            if len(parts) < 2:
                print(f"Skipping invalid folder name: {directory_name}")
                continue

            chapter_title = parts[1].strip()

            # Generate the new directory name with chapter number
            new_directory_name = f"Chapter {chapter_number} - {chapter_title}"

            # Create the new path
            new_directory_path = os.path.join(root, new_directory_name)

            try:
                # Rename the directory
                os.rename(directory_path, new_directory_path)
                print(f"Renamed '{directory_path}' to '{new_directory_path}'")

                # Increment chapter number
                chapter_number += 1
            except Exception as e:
                print(f"An error occurred: {e}")


if __name__ == "__main__":
    # Input the directory path
    directory_path = input("paste the folder name: ")

    # Rename the directories within the specified path
    rename_directories_in_path(directory_path)
