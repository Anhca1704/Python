a=int(input())
s=0
c=0
i=1
while i*i <=a:
	if a % i ==0 :
		if i *i ==a:
			s+=i
			c+=1
		else:
		    s+=i+a/i
		    c+=2	
	i+=1
print(s," ",c)