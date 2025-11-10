k=int(input())
A=list(map(int,input().split()))
for i in A:
	x=k-i
	if A.count(x)!=0: 
		print(i," ",x)
		A.remove(x)