"""
This program - once ran - will clean the download folder of the pc,
putting them into an archive fodler within the User's "Documents" 
Folder.
"""

import os
import shutil

# Initiate our source and destination folders.
src_folder = f'{os.path.expanduser("~")}\\Downloads'
destination_folder = f'{os.path.expanduser("~")}\\Documents'

# Arrays to hold our files and directories
dirs = []
files = []
counter = 0

# Gets all the files and directories within your downloads folder
for dirpath, dirname, filename in os.walk(src_folder):
    # If the path is the same as the C:\...\Downloads dir
    if dirpath == src_folder:
        files.append(filename)
        continue
    
    
    # Gets ONLY the directory name and not what's before.
    mainFolders = dirpath.replace(src_folder, "")

    # Gets the main directories within the downloads folder.
    try:
        if dirs[counter] in mainFolders:
            continue
        else: 
            dirs.append(mainFolders)
            counter += 1
    except IndexError:
        # Adds the initial directory into the dirs array if there is none (IndexError)
        dirs.append(dirpath.replace(src_folder, ""))

# Creates a directory in your documents folder labaled "Archive"
try:
    archive = os.path.join(destination_folder, "Archive")
    os.mkdir(archive)
except FileExistsError:
    pass

# Changes destination to folder we created
destination_folder = f'{os.path.expanduser("~")}\\Documents\\Archive'

# Map all the kinds of extensions we have and their respective category
map = {
    "Documents" : [".doc", ".docx", ".pdf", ".ppt", ".pptx", ".xls", ".xlsx"],
    "Images" : [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".tif", ".tiff"],
    "Audio" : [".mp3", ".wav", ".wma", ".aac", ".flac", ".ogg"],
    "Videos" : [".mp4", ".avi", ".mkv", ".wmv", ".flv", ".mov", ".m4v"],
    "Compressed" : [".zip", ".rar", ".7z", ".tar", ".gz", ".bz2", ".xz"],
    "Executable" : [".exe", ".msi", ".dmg"],
    "Web-Related" : [".html", ".css", ".js", ".php", ".asp", ".xml"],
    "Programming" : [".py", ".java", ".cpp", ".c", ".h", ".cs", ".rb", ".php", ".pl", ".sh"],
    "Text-Markup" : [".md", ".markdown", ".txt"],
    "Data" : [".dat", ".csv", ".json", ".sql"],
    "Miscellaneous" : [".log", ".bak", ".tmp"]
}

# We then move each file into our Archive
for file in files[0]:
    extension = os.path.splitext(file)
    file_name = extension[0]
    file_extension = extension[1]
    
    category = next((category for category, extensions in map.items() if file_extension in extensions), "Directories")
    
    try:
        folder = os.path.join(archive, category)
        os.mkdir(folder)
    except FileExistsError:
        pass
    
    fileFullPath = os.path.join(src_folder, file)
    shutil.move(fileFullPath, folder)
    
    
# We then move each directory into our Archive  
for dir in dirs:
    try:
        folder = os.path.join(archive, "Directories")
        os.mkdir(folder)
    except FileExistsError:
        pass
    shutil.move(src_folder + dir, folder)


    
    
    
    
    
    

    
