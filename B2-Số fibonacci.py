def fibo(n):
	A=[0,1]
	while A[-1]+A[-2]<=n:
		A.append(A[-1]+A[-2])
	return A
n=int(input())
B=fibo(10**5)
for i in range(n-1):
	print(B[i],end=" ")
