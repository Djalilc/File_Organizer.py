#give it a folder 
#it sorts files into subfolders: 
    #images 
    #videos
    #PDFs 
    #documents
    #Others

#section to upload a file
#section to process the file and indentify type
#section to move said file to that subfolder 

#Thinking model: 
#Ask user for folder path
#look at all files in that folder 
#detect file extension
#Decide which folder it belongs to 
#Move the file there
#Handle errors 


from tkinter import Tk, filedialog
from pathlib import Path

Tk().withdraw()  # hides the Tk window
folder_path = filedialog.askdirectory()
print(folder_path)

path = Path(folder_path)

images = [".png", ".jpg", ".jpeg", ".gif", ".bmp", ".tiff", ".webp", ".svg"]
Documents = [".pdf", ".doc", ".docx", ".txt", ".rtf", ".odt", ".md"]
spreadsheets = [".xls", ".xlsx", ".csv", ".ods"]
presentations = [".ppt", ".pptx", ".odp"]
scripts = [".py", ".js", ".ts", ".html", ".css", ".c", ".cpp", ".h", ".hpp", ".java", ".cs", ".php", ".rb", ".go", ".rs", ".swift"]
DataFormats = [".json", ".xml", ".yaml", ".yml", ".sql", ".db", ".sqlite", ".parquet"]
Audio = [".mp3", ".wav", ".aac", ".flac", ".ogg", ".m4a"]
video = [".mp4", ".mov", ".avi", ".mkv", ".flv", ".wmv"]
archives = [".zip", ".rar", ".7z", ".tar", ".gz", ".bz2"]
executables = [".exe", ".msi", ".bat", ".sh", ".app"]
other = [".iso", ".bin", ".bak", ".tmp"]

categories = {
    "images": images,
    "Documents": Documents,
    "spreadsheets": spreadsheets,
    "presentations": presentations,
    "scripts": scripts,
    "DataFormats": DataFormats,
    "Audio": Audio,
    "video": video,
    "archives": archives,
    "executables": executables,
    "other": other
}

for item in path.iterdir():
    if item.is_file():                     # Only work on files
        ext = item.suffix.lower()
        print("Extension:", ext)

        for folder_name, ext_List in categories.items():

            if ext in ext_List:            # Found matching category

                # Create folder (if not exists)
                new_folder = path / folder_name
                new_folder.mkdir(exist_ok=True)

                # Move file into that folder
                destination = new_folder / item.name
                item.rename(destination)

                break  # stop looping categories once matched

