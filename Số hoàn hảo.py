n=int(input())
s=1
i=2
while i**2<n:
	if n%i==0:
		if i*i==n:
			s+=i
		else:
			s+=i+n/i
	i+=1
if s==n:
	print("Yes")
else:
	print("No")