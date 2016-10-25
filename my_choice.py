num=10
c=1
def factorial(n) :
	if n!=0   :
		global c
		c=c*n
		factorial(n-1)
	else :
		print c
		return 0
factorial(abs(num))
