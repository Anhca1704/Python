def fibo(n):
	A=[0,1]
	while A[-1]+A[-2]<=n:
		A.append(A[-1]+A[-2])
	return A
n=int(input())
print(fibo(n))