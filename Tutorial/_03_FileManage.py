import os.path

def getFileExtension(fileName):
    return os.path.splitext(fileName)[1]

### File Managec
## Relative path / Absolute path
# readmeFile = open("../README.md", "r")
# print(readmeFile.readable())
# print(readmeFile.readline())
# fileArray = readmeFile.readlines()
# print(fileArray)
# print("This is python File: \t" + str(readmeFile))
# readmeFile.close() # always close a file after open
#
# ## Apend file
# readmeFile = open("../README.md", "a")
# readmeFile.write("\nThis is to append a file. \n")
# readmeFile.close()

