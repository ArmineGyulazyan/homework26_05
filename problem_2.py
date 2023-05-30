import random

count = 0
while count < 50:
	rand_num = random.randint(3,6)
	count+=1
	print("Random integer"+str(count)+" between 3 and 6 is = ", rand_num)