import math
def snt(a):
	if a<2: 
		return False
	for i in range(2,int(math.sqrt(a)+1)):
		if a%i==0:
			return False
	return True
c=0
A=list(map(int,input().split()))
for i in A:
	if snt(i):
		c+=1
print(c)

