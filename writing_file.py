file=open('file.txt','w')
file.write('this is the new text .')
file.close()
file1=open('file.txt','r')
print(file1.read())
