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

images = ['.png', '.jpeg']
text = ['.pdf', '.docx']
asdf
asdf
asdf
other = []


for item in path.iterdir():
    ext = item.suffix.lower()
    if item.is_file(): 
        print("Extension:", ext)

#create four lists and iterate through each one to find out if it belongs to that list and if it doesnt then move onto the next list

