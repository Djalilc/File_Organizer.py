"""
File Organizer – Micro Project 1
--------------------------------
This script automatically sorts files in a selected directory into category
folders based on their file extension. The goal is to build real engineering
discipline: clean structure, clear categories, robust handling of edge cases,
and extensible design.

Key Concepts Practised:
- pathlib.Path for filesystem operations
- Mapping file suffixes to semantic categories
- Creating folders programmatically
- Handling filename collisions safely
- Iterating over directory contents with defensive checks
- Foundation for future Tkinter GUI wrapper

This project establishes the base pattern for all 20 micro-projects:
small, shippable, robust, and clean.
"""


from tkinter import Tk, filedialog
from pathlib import Path

Tk().withdraw()  # hides the Tk window
folder_path = filedialog.askdirectory()
print(folder_path)

path = Path(folder_path)

Images = [".png", ".jpg", ".jpeg", ".gif", ".bmp", ".tiff", ".webp", ".svg"]
Documents = [".pdf", ".doc", ".docx", ".txt", ".rtf", ".odt", ".md"]
Spreadsheets = [".xls", ".xlsx", ".csv", ".ods"]
Presentations = [".ppt", ".pptx", ".odp"]
Scripts = [".py", ".js", ".ts", ".html", ".css", ".c", ".cpp", ".h", ".hpp", ".java", ".cs", ".php", ".rb", ".go", ".rs", ".swift"]
DataFormats = [".json", ".xml", ".yaml", ".yml", ".sql", ".db", ".sqlite", ".parquet"]
Audio = [".mp3", ".wav", ".aac", ".flac", ".ogg", ".m4a"]
Video = [".mp4", ".mov", ".avi", ".mkv", ".flv", ".wmv"]
Archives = [".zip", ".rar", ".7z", ".tar", ".gz", ".bz2"]
Executables = [".exe", ".msi", ".bat", ".sh", ".app"]
Other = [".iso", ".bin", ".bak", ".tmp"]

categories = {
    "images": Images,
    "Documents": Documents,
    "spreadsheets": Spreadsheets,
    "presentations": Presentations,
    "scripts": Scripts,
    "DataFormats": DataFormats,
    "Audio": Audio,
    "video": Video,
    "archives": Archives,
    "executables": Executables,
    "other": Other
}

for item in path.iterdir():
    if item.is_file():             # Only work on files
        ext = item.suffix.lower()
        print("Extension:", ext)

        for folder_name, ext_List in categories.items():

            if ext in ext_List:    # Found matching category

                # Create folder (if not exists)
                new_folder = path / folder_name
                new_folder.mkdir(exist_ok=True)

                # Move file into that folder
                destination = new_folder / item.name
                item.rename(destination)

                break  # stop looping categories once matched

