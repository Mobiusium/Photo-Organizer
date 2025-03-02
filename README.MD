# Photo Organizer

## Overview

This Python script organizes photos into folders based on their creation date. It extracts metadata from image files and sorts them into directories named after their creation date. If metadata is unavailable, it falls back to the file's last modified timestamp.

## Features

- Extracts creation dates from image metadata (EXIF data)
- Falls back to the file's last modified date if metadata is missing
- Organizes photos into date-based folders automatically
- Handles errors gracefully without interrupting the process
- Uses `tqdm` to display a progress bar while processing files

## Prerequisites

Ensure you have Python installed (version 3.x recommended). The script requires the following Python libraries:

- `PIL` (Pillow) for image processing
- `tqdm` for displaying progress bars

Install the dependencies using pip:

```bash
pip install pillow tqdm
```

## Usage

1. Run the script:
   ```bash
   python photo_organizer.py
   ```
2. Enter the source folder path containing photos when prompted.
3. Enter the destination folder path where organized photos should be stored.
4. The script will process the files and move them into folders named after their creation dates.

## Example

**Before Running the Script:**

```
/source-folder/
    photo1.jpg
    photo2.png
    image3.jpeg
```

**After Running the Script:**

```
/destination-folder/
    2024-02-15/
        photo1.jpg
        image3.jpeg
    2023-09-10/
        photo2.png
```

## Error Handling

- If an image lacks EXIF data, the script will use the last modified date.
- If a file cannot be moved, it will be skipped without stopping execution.
- Hidden system files (e.g., `._filename`) are ignored.

## License

This project is licensed under the MIT License.
