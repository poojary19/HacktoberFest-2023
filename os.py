import os.path
import sys
fname=input("enter the filename:")
if not os.path.isfile(fname):
    print("File",fname,"doesnot exist")
    sys.exit(0)
infile=open(fname,"r")
lineList=infile.readlines()
for i in range(10):
    print(i+1,":",lineList[i])
word=input("enter the word:")
cnt=0
for line in lineList:
    cnt += line.count(word)
print("words",word,"appears",cnt,"times in the file")
