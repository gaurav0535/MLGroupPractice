# File operations
try:

	fd = open('wipro.txt','r')
	print 'the file handle opened at : ' , fd
	print 'the file opened for operations at' , fd.name
	print ' the statis of the file whether closed : ', fd.closed
	print ' the mode of the file opened :' , fd.mode
except IOError,e:
	print ' the file you are trying is having error'
	print 'Error: ' , e
except exception, e:
	print 'Error: ' , e
finally :
	fd.close()
	
