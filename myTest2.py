

i = input("Enter your number:")

if i<2 or i>9:
	print "you input wrong number"
else:
	for j in range(1,10):
		print i*j
