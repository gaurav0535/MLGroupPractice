#sample scriptimg for file handling

try:
	fd = open ('wipro.txt','r')
	print ' the file opened for operations is : ', fd.name
	print ' the status of file is : ', fd.closed
	print ' the mode of the file opened is " ', fd.mode
	print ' enabling read operations for file : '
	print  " read operations on the file :" , fd.read(10)