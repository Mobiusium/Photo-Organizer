import os
import shutil
from datetime import datetime
from PIL import Image, UnidentifiedImageError
from PIL.ExifTags import TAGS
from tqdm import tqdm

__author__ = "Your Name"
__email__ = "your.email@example.com"
__version__ = "1.0.0"

def get_date_created(file_path):
    """
    Extract the creation date from the file or EXIF data.

    Args:
        file_path (str): The path to the image file.

    Returns:
        datetime.date: The creation date of the image, or None if it cannot be determined.
    """
    try:
        # Open image and get EXIF data
        image = Image.open(file_path)
        exif_data = image._getexif()
        if exif_data:
            for tag, value in exif_data.items():
                if TAGS.get(tag) == "DateTimeOriginal":
                    return datetime.strptime(value, "%Y:%m:%d %H:%M:%S").date()
    except UnidentifiedImageError:
        pass
    except Exception:
        pass

    # Fallback to file's modification date
    try:
        timestamp = os.path.getmtime(file_path)
        return datetime.fromtimestamp(timestamp).date()
    except Exception:
        return None

def organize_photos(source_folder, destination_folder):
    """
    Organize photos into folders based on their creation date.

    Args:
        source_folder (str): The path to the source folder containing photos.
        destination_folder (str): The path to the destination folder where organized photos will be stored.
    """
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    for root, _, files in os.walk(source_folder):
        for file_name in tqdm(files, desc="Organizing photos", colour="blue"):
            if file_name.startswith("._"):
                continue

            file_path = os.path.join(root, file_name)

            # Get the creation date
            creation_date = get_date_created(file_path)
            if not creation_date:
                continue

            # Create the target directory based on the date
            date_folder = os.path.join(destination_folder, str(creation_date))
            if not os.path.exists(date_folder):
                os.makedirs(date_folder)

            try:
                # Move the file
                shutil.move(file_path, os.path.join(date_folder, file_name))
            except Exception:
                pass

if __name__ == "__main__":
    # Ask the user for source and destination folder paths
    source_folder = input("Enter the source folder path containing photos: ").strip().strip("'\"")
    destination_folder = input("Enter the destination folder path: ").strip().strip("'\"")

    # Validate input paths
    if not os.path.exists(source_folder):
        print(f"Error: Source folder '{source_folder}' does not exist.")
    else:
        organize_photos(source_folder, destination_folder)