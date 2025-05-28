import os
import shutil
from pathlib import Path
from filecmp import cmp
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def get_folder_path(folder_name):
    """Get the path to a specific folder in the user's home directory."""
    return Path.home() / folder_name

def create_target_folders(file_type_folders):
    """Create target folders if they don't exist."""
    for folder in file_type_folders.keys():
        target_path = get_folder_path(folder)
        target_path.mkdir(parents=True, exist_ok=True)

def remove_exe_files(downloads_path):
    """Remove .exe files from the Downloads folder."""
    for file in downloads_path.glob('*.exe'):
        try:
            file.unlink()
            logging.info(f"Deleted: {file}")
        except Exception as e:
            logging.error(f"Error deleting {file}: {e}")

def organize_files_by_type(downloads_path, file_type_folders):
    """Organize files by type into their respective folders."""
    for file in downloads_path.iterdir():
        if file.is_file():
            moved = False
            for folder, extensions in file_type_folders.items():
                if file.suffix.lower() in extensions:
                    target_path = get_folder_path(folder) / file.name
                    try:
                        shutil.move(str(file), str(target_path))
                        logging.info(f"Moved: {file} to {target_path}")
                        moved = True
                    except Exception as e:
                        logging.error(f"Error moving {file} to {target_path}: {e}")
                    break
            if not moved:
                target_path = get_folder_path('Others') / file.name
                try:
                    shutil.move(str(file), str(target_path))
                    logging.info(f"Moved: {file} to {target_path}")
                except Exception as e:
                    logging.error(f"Error moving {file} to {target_path}: {e}")

def find_duplicates_by_name(downloads_path):
    """Find duplicate files by examining file names and comparing their contents."""
    files = sorted(downloads_path.iterdir())
    duplicates = []

    for file in files:
        if file.is_file():
            is_duplicate = False
            for class_ in duplicates:
                if cmp(file, class_[0], shallow=False):
                    class_.append(file)
                    is_duplicate = True
                    break
            if not is_duplicate:
                duplicates.append([file])

    return duplicates

def remove_duplicate_files(duplicates):
    """Remove duplicate files, keeping only the latest one."""
    for class_ in duplicates:
        if len(class_) > 1:
            latest_file = max(class_, key=lambda f: f.stat().st_mtime)
            for file in class_:
                if file != latest_file:
                    try:
                        file.unlink()
                        logging.info(f"Deleted duplicate: {file}")
                    except Exception as e:
                        logging.error(f"Error deleting duplicate {file}: {e}")

def main():
    downloads_path = get_folder_path('Downloads')

    file_type_folders = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff'],
        'Documents': ['.pdf', '.doc', '.docx', '.xls', '.xlsx', '.ppt', '.pptx', '.txt'],
        'Videos': ['.mp4', '.avi', '.mov', '.mkv'],
        'Music': ['.mp3', '.wav', '.aac', '.flac'],
        'Archives': ['.zip', '.rar', '.tar', '.gz', '.7z'],
        'Others': []
    }

    create_target_folders(file_type_folders)
    remove_exe_files(downloads_path)
    organize_files_by_type(downloads_path, file_type_folders)
    duplicates = find_duplicates_by_name(downloads_path)
    remove_duplicate_files(duplicates)

    logging.info("Downloads folder cleaned and organized.")

if __name__ == "__main__":
    main()