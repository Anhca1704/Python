a=int(input())
import math
n=10**5
A=[True]*(n+1)
A[1]=A[0]=False
for i in range (2,int(math.sqrt(n))+1):
	if A[i]:
		for j in range(i*i,n+1,i):
			A[j]=False
for i in range(n):
	if A[i] and (i>a):
		print(i)
		break