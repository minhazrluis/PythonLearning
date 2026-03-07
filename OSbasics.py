import os
import shutil  # for moving files

folder = os.getcwd()

# define where each extension goes
destinations = {
    ".py": "Python Files",
    ".csv": "Data Files",
    ".json": "Data Files",
    ".pdf": "Documents",
    ".docx": "Documents",
    ".txt": "Documents"
}

for filename in os.listdir(folder):
    # get file extension
    _, ext = os.path.splitext(filename)
    # check if it's in destinations
    if ext in destinations:
        # create subfolder if it doesn't exist
        subfolder = destinations[ext]
        os.makedirs(subfolder, exist_ok=True)
        # move the file
        shutil.move(filename, os.path.join(subfolder, filename))