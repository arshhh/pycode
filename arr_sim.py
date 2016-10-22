a=[1,2,3,4]
i=-1
k=0
print 'print loop in reverse'
def something (i,k):
  	
	print a[i]
	k=k+1	
	if  k!=4	:
		something ( i-1, k )
	else :
		return 0;

something(-1,0)
