# Write your solution for 1.4 here!

def is_prime(x):
	if (x==1):
		return False
	elif (x==2):
		return True
	else:
		for i in range(2,x):
			if(x % i==0):
				return False
		return True
print(is_prime(5191))