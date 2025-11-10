A=list(map(int,input().split()))
a=b=A[0]
for i in A:
	if i>a:
		a=i
	if i<b:
		b=i
print(a," ",b)