import os
import sys

READONLY = "r"
READWRITE = "w"
APPEND = "a"

async def readFile(file):
    f = open(file, READONLY)
    return f.read()


async def writeFile(file, content):
    f = open(file, READWRITE)
    f.write(content)

def readFileSync(file):
    f = open(file, READONLY)
    return f.read()


def writeFileSync(file, content):
    f = open(file, READWRITE)
    f.write(content)

async def readDir(dir):
    return os.listdir(dir)

def readDirSync(dir):
    return os.listdir(dir)

def readDirString(dir):
    return ", ".join(os.listdir(dir))

def move(file, dest):
    with open(file, 'r') as f:
        content = f.read()

    with open(f"{dest}/{file}","w") as f:
        f.write(content)

    os.remove(file)



def copy(file, dest):
    with open(file, 'r') as f:
        content = f.read()

    with open(f"{dest}/{file}","w") as f:
        f.write(content)
