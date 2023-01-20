from dirsync import sync
from pathlib import Path
import io
import os
import subprocess
import shutil


def createExe(userInput):
    with io.open("sync.py",'w',encoding='utf8') as f:
        f.writelines(["from dirsync import sync\n", f"sync({userInput[0]}, {userInput[1]}, 'sync')"])
        f.close()

    subprocess.run("pyinstaller --onefile sync.py", shell=True)
    print(f"sync.exe created at {Path.cwd()}\dist")
    
def clearDir():
    try:
        print(f"{Path.cwd()}\sync.py")
        os.remove(f"{Path.cwd()}\sync.py")
    except OSError as e:
        print("Error: %s - %s." % (e.filename, e.strerror))
        
    try:
        print(f"{Path.cwd()}\sync.spec")
        os.remove(f"{Path.cwd()}\sync.spec")
    except OSError as e:
        print("Error: %s - %s." % (e.filename, e.strerror))
        
    try:
        print(f"{Path.cwd()}\\build")
        shutil.rmtree(f"{Path.cwd()}\\build")
    except OSError as e:
        print("Error: %s - %s." % (e.filename, e.strerror))
    
def promt():
    source_path = input("Source path: ")
    source_path = f"r\"{source_path}\""
    
    target_path = input("Target path: ")
    target_path = f"r\"{target_path}\""
    
    return [source_path, target_path]

print("==================SyncR==================")
print("This tool creates an .exe file which syncs\n2 selected folders with a simple double click.")
print("\nBy KDesp73 - 2023\n\n")

userInput = promt()
createExe(userInput)
clearDir()

print("\n")
input("Press any key to continue...")