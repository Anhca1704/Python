import math
n=int(input())
def ktra(a):
	if a<2: return False
	for i in range(2,int(math.sqrt(a)+1)):
		if a%i==0:
			return False
	return True
for i in range(2,int(math.sqrt(n)+1)):
	if n%i==0 and ktra(i):
		print(i)
		if i!=n//i and ktra(n/i):
			print(n/i)
