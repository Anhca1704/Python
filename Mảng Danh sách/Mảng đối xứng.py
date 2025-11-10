A=list(map(int,input().split()))
x=True
for i in range((len(A)-1)//2):
	if A[i]!=A[len(A)-1-i]:
		x=False
		break
if x: print("Yes")
else: print("No")

