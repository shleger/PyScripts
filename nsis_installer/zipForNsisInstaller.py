__author__ = 'shleger'

import shutil
import sys
import os

# os.system("dir")

if sys.argv.__len__() != 3:
    raise Exception("ZIP location is not defined: usage: ARCHIVE_PATH ARCHIVE_FOLDER ")
    exit(0)

# ver = None
with open("nsis_installer/prop.properties") as f:
    lines = f.readlines()

for line in lines:
    if line.__contains__("version"):
        ver = line.split("=")[1]


if ver is None:
    raise Exception("ver == null")


ARCHIVE_PATH = sys.argv[1]
ARCHIVE_FOLDER = sys.argv[2]

#shutil.make_archive(ARCHIVE_PATH , "zip", ARCHIVE_FOLDER)
# shutil.copyfile()

str = r"D:\9\edo.zip"
last = ARCHIVE_PATH.rfind("/")
dir = str[:last]

print(ARCHIVE_PATH)

#shutil.copyfile("d:/9/edo.zip", "D:/9/1/df.zip")

'''

import zipfile
import os

target_dir = 'D:/9/edo/'
zip = zipfile.ZipFile('D:/9/example.zip', 'w', zipfile.ZIP_DEFLATED)
rootlen = len(target_dir)
for base, dirs, files in os.walk(target_dir):
    for file in files:
        fn = os.path.join(base, file)
        zip.write(fn, fn[rootlen:])

'''

