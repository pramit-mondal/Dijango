file=open('file.txt','r')# want to read this file,'w'' means want to write something in this file,'a' means append to the ending of the file.

#print(file.readable())#print that the file is readable or not-True or False.

#print(file.readline())#only read the first line of text file.

#print(file.readlines())#every thing of list .and also can used -> file.readlines()[0]-to read only first line.

for lines in file.readlines():
    print(lines)
file.close()