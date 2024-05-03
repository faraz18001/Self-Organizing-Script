import os
import shutil

# Source directory
source_dir = r'C:\Users\faraz\Downloads'

# Get the current working directory
current_dir = os.getcwd()

# Get the list of files in the source directory
files = os.listdir(source_dir)

# Get the list of file extensions
extensions = set()
for file in files:
    _, file_extension = os.path.splitext(file)
    extensions.add(file_extension.lower())

# Create folders for each file extension in the current working directory
def create_folders():
    for extension in extensions:
        folder_name = extension[1:].upper()  # Remove the leading dot and convert to uppercase
        folder_path = os.path.join(source_dir, folder_name)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
            print(f"Created folder: {folder_name}")

# Move files to their respective folders
def move_files():
    for file in files:
        _, file_extension = os.path.splitext(file)
        folder_name = file_extension[1:].upper()
        folder_path = os.path.join(source_dir, folder_name)
        if os.path.exists(folder_path):
            source_path = os.path.join(source_dir, file)
            destination_path = os.path.join(folder_path, file)
            shutil.move(source_path, destination_path)
            print(f"Moved {file} to {folder_name} folder.")

# Remove folders created in the current working directory
def remove_folders():
    for folder in os.listdir(current_dir):
        folder_path = os.path.join(current_dir, folder)
        if os.path.isdir(folder_path):
            try:
                os.rmdir(folder_path)
                print(f"Removed folder: {folder}")
            except OSError:
                print(f"Error: Unable to remove folder: {folder}")

# Create folders
create_folders()

# Move files to their respective folders
move_files()

# Print the list of created folders
print("\nList of created folders:")
for index, folder in enumerate(sorted(os.listdir(current_dir)), start=1):
    print(f"{index}. {folder}")

# Remove folders
#remove_folders()