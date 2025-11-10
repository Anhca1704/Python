import math
n=int(input())
def ktra(a):
	A=[]
	c=0
	while a%2==0:
			c+=1
			a//=2
	if c!=0:
		A.append((2,c))
	for i in range(3,int((math.sqrt(a))+1),2):
		c=0
		while a%i==0:
			c+=1
			a//=i
		if c!=0:
			A.append((i,c))
		if a==1:
			break
	return A
print(ktra(n))
