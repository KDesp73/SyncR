# MIT License
#
# Copyright (c) 2023 Konstantinos Despoinidis
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


from dirsync import sync
from pathlib import Path
import io
import os
import subprocess
import shutil
import sys

slash = '/' if (os.name.__contains__("posix")) else '\\'


def program(userInput):

    program = f"""from dirsync import sync
import sys\n

src = \"{userInput[0]}\"
target = \"{userInput[1]}\"

if sys.argv.__len__() != 1 and (sys.argv[1] == \"-r\" or sys.argv[1] == \"--reverse\"):
    src, target = target, src\n

sync(src, target, 'sync')
input(\"Press any key to continue...\")\n
"""
    return program


def createExe(userInput):
    with io.open("sync.py", 'w', encoding='utf8') as f:
        f.writelines(program(userInput))
        f.close()

    subprocess.run("pyinstaller --onefile sync.py", shell=True)
    print(f"sync executable created at {Path.cwd()}/dist")


def clearDir():
    try:
        print(f"{Path.cwd()}{slash}sync.py")
        os.remove(f"{Path.cwd()}{slash}sync.py")
    except OSError as e:
        print("Error: %s - %s." % (e.filename, e.strerror))
    try:
        print(f"{Path.cwd()}{slash}sync.spec")
        os.remove(f"{Path.cwd()}{slash}sync.spec")
    except OSError as e:
        print("Error: %s - %s." % (e.filename, e.strerror))
    try:
        print(f"{Path.cwd()}{slash}build")
        shutil.rmtree(f"{Path.cwd()}{slash}build")
    except OSError as e:
        print("Error: %s - %s." % (e.filename, e.strerror))


def promt():
    source_path = input("Source path: ")
    source_path = f"r\"{source_path}\""

    target_path = input("Target path: ")
    target_path = f"r\"{target_path}\""

    return [source_path, target_path]


if __name__ == "__main__":
    if sys.argv.__len__() != 3:
        print("==================SyncR==================")
        print("This tool creates an executable file which syncs\n2 selected folders with a simple double click.")
        print("\nBy KDesp73 - 2023\n\n")

        userInput = promt()

    else:
        userInput = sys.argv[1:3]
        print(userInput)

    createExe(userInput)
    clearDir()
    print("\n")
    input("Press any key to continue...")
