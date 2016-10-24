a=10
def hello (n,c) :
	if n!=0   :
		c=c*n
		hello ( n-1,c )
	else :
		print c
		return 0



hello (a,1)
