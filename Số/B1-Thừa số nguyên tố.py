import math
n=int(input())
def ktra(a):
	A=[]
	if a%2==0:
		A.append(2)
		a/=2
	for i in range(3,int((math.sqrt(a))+1),2):
		if a%i==0:
			A.append(i)
			a//=i
		if a==1: break
	return A
print(ktra(n))