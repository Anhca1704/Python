import math
def sth(a):
	x=y=str(a)
	y=y[::-1]
	if x==y : 
		return True 
c=0
A=list(map(int,input().split()))
for i in A:
	if sth(i):
		c+=1
print(c)

