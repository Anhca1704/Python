import math
a,b=map(int,input().split())
x=int(math.sqrt(a)/10*10)
y=int(math.sqrt(b)/10*10)
for i in range(x,y+1):
	print(i**2)
