import os
import shutil

# Mapping of folder names to corresponding file extensions
FILE_CATEGORIES = {
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".csv"],
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".webp"],
    "Archives": [".zip", ".tar", ".gz", ".rar"],
    "Scripts": [".py", ".js", ".html", ".css", ".sql"],
}

def organize_folder(target_directory):
    """
    Scans the target directory and moves files into organized subfolders
    based on their extensions.
    """
    if not os.path.exists(target_directory):
        print(f"Directory not found: {target_directory}")
        return

    for filename in os.listdir(target_directory):
        file_path = os.path.join(target_directory, filename)

        if os.path.isfile(file_path):
            _, extension = os.path.splitext(filename)
            moved = False

            for category, extensions in FILE_CATEGORIES.items():
                if extension.lower() in extensions:
                    dest_folder = os.path.join(target_directory, category)
                    os.makedirs(dest_folder, exist_ok=True)
                    shutil.move(file_path, os.path.join(dest_folder, filename))
                    print(f"Moved {filename} -> {category}/")
                    moved = True
                    break

            if not moved:
                dest_folder = os.path.join(target_directory, "Others")
                os.makedirs(dest_folder, exist_ok=True)
                shutil.move(file_path, os.path.join(dest_folder, filename))
                print(f"Moved {filename} -> Others/")

if _name_ == "_main_":
    print("--- File Organizer Script Ready ---")
    print("Call organize_folder(path) with your target directory path.")
