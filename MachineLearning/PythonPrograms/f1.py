# File operations

fd = open('wipro.txt','r')
print 'the file handle opened at : ' , fd
print 'the file opened for operations at' , fd.name
print ' the statis of the file whether closed : ', fd.closed
print ' the mode of the file opened :' , fd.mode
fd.close()
print ' the status of the file after closing:', fd.closed