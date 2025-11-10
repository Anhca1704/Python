A=list(map(int,input().split()))
for i in range((len(A)-1)//2):
	t=A[i]
	A[i]=A[len(A)-1-i]
	A[len(A)-1-i]=t
print(A)
