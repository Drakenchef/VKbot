import os
import shutil
import subprocess
import datetime
import sys


def make_dir():
    path = os.getcwd()
    if not os.path.exists("Ознакомительная папка"):
        os.mkdir("Ознакомительная папка")
        os.mkdir("Ознакомительная папка/Тема A")
        os.mkdir("Ознакомительная папка/Тема B")
    files = os.listdir()
    for file in files:
        if file[:4] == "task" and file[5] == "A":
            shutil.copy(str(file), "./Ознакомительная папка/Тема A/" + file)
        if file[:4] == "task" and file[5] == "B":
            shutil.copy(str(file), "./Ознакомительная папка/Тема B/" + file)


def py_file(path):
    files = os.listdir(path)
    for folder in files:
        if os.path.isdir(path + folder + "/"):
            print("Folder: ", folder)
            tpath = path + folder + "/"
            list = os.listdir(tpath)
            for file in list:
                with open(file, "r", encoding="utf-8") as f:
                    for line in f:
                        if "def" in line:
                            print(f"\tFunction: {line.replace('def', '').strip().replace(':', '')}")
                if file[-3:] == ".py":
                    t = datetime.datetime.now()
                    result = subprocess.run([sys.executable, tpath + file], input="", capture_output=True, text=True)
                    dt = datetime.datetime.now()-t
                    print("\tRunning time: ", dt.seconds, "s ", dt.microseconds, "ms")
                    print("\tOutput: ", result.stdout)


if __name__ == "__main__":
    make_dir()
    py_file(os.getcwd() + "/Ознакомительная папка/")
