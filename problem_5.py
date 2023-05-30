sum = 0
for perfect_num in range(1,10000):
	for divisor in range(1,perfect_num+1):
		if perfect_num % divisor == 0:
			sum+=divisor
	if sum-perfect_num != perfect_num:
		sum = 0
	else:
		print(perfect_num," is a perfect number")