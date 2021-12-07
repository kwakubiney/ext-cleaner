import os
from sys import argv


path = "C:\\Users\\Kwaku Biney\\Desktop"

def delete_files(path, extension):
    dirs = os.listdir(path)
    files = []
    for x in dirs:
        if str(x).endswith(f"{extension}"):
            files.append(x)
    for x in files:
        os.remove((os.path.join(path, x)))


delete_files(argv[1],argv[2])


