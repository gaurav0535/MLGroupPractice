#sample scriptimg for file handling


fd = open ('wipro.txt','w')
print ' the file opened for operations is : ', fd.name
print ' the status of file is : ', fd.closed
print ' the mode of the file opened is " ', fd.mode

print ' Enabling write operations for file'

text =  " this line has been added from file operations\n Next line"
fd.write(text)

fd.close()