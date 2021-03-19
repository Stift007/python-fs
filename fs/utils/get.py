import os

class InvalidPath(Exception):
    """
    Trying to access Invalid Path
    """
    pass

class DangerousPath(InvalidPath):
    """
    Gets thrown when you try to access a dangerous Path(Like C:\\:$i30:$bitmap)
    """

def path(path,filename):
    """
    Recursively look for a file from a Root Directory
    """
    dangerouspaths = ["c:\\:$i30:$bitmap","\\\\.\\globalroot\device\condrv\kernelconnect"]
    if path.lower() in dangerouspaths:
        raise DangerousPath(path)
    else:
        if os.path.exists(path):
            for root, dirs,files in os.walk(path):
                for file in files:
                    if file == filename:
                        return os.path.join(root,filename)
        else:
            raise InvalidPath(path)

def content(file):
    """
    Get the Content of a File
    """

    with open(file,"r") as f:
        return f.read()
