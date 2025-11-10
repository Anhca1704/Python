def gcd(a,b):
	while b!=0:
		c=a
		a=b
		b=c%a 
	return a
A=list(map(int,input().split()))
for i in range(len(A)-1):
	for j in range(i,len(A)-1):
		if gcd(A[i],A[j])==1:
			print(A[i],' ',A[j])