import math
n=int(input())
A=[True]*(n+1)
A[1]=A[0]=False
for i in range (2,int(math.sqrt(n))+1):
	if A[i]:
		for j in range(i*i,n+1,i):
			A[j]=False
print([i for i in range(n) if A[i]])