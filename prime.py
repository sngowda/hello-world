n=int(input("enetr number: "))
for i in range(1,n+1):
	if all(i%j  for j in range(2,i)):
		if(i>1):
			print (i)