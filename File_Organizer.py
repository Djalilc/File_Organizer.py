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

Tk().withdraw() # hides the little Tk window
folder_path = filedialog.askdirectory() # opens the folder picker
print(folder_path)

#folder path right now is just a text string its not a folder so it can't list files move them create folders etc.
#it needs something smarter
#path object is a part of the pathlib module 
#pythongs way of recognizing an acutal folder which you can perform tasks on

path = Path(folder_path) #converts the string into a path object that python can perform operations on 

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


for item in path.iterdir():
    ext = item.suffix.lower()
    if item.is_file(): 
        print("Extension:", ext)

#create four lists and iterate through each one to find out if it belongs to that list and if it doesnt then move onto the next list

