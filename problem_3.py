def expression(x,y):
	absolute_val = abs(x-y)
	divided_val = absolute_val / x
	result = divided_val + y
	print("The result is = ", result)

while True:
	num1 = input("Please enter the first number: ")
	num2 = input("Please enter the second number: ")
	if (num1 != '0'):
		fl_num1 = float(num1)
		fl_num2 = float(num2)
		expression(fl_num1,fl_num2)
		break
	else:
		print("Wrong Input! \n")

