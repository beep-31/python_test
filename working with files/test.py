import os
import pyperclip 

totalSize = 0
cwd = os.getcwd()

for file in os.listdir(cwd):
	totalSize = totalSize + os.path.getsize(os.path.join(cwd, file))
print(totalSize)