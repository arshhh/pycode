a=[1,2,3,4]
p=-1
k=0
print 'print loop in reverse'
def something (p,k):
  	
	print a[p]
	k=k+1	
	if  k!=4	:
		something ( p-1, k )
	else :
		return 0;

something(-1,0)
