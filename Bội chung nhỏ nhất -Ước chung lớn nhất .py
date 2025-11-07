a,b=map(int,input().split())
n=b
def tim(a,b):
	while b>0:
		c=a%b
		a=b
		b=c	
	return a
print(tim(a,b),(a*b)//tim(a,b))

