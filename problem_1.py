while True:
	weight_KG = input("Please enter your weight in kilograms: ")
		
	if weight_KG.replace('.', '', 1).isdigit():
		weight_P = float(weight_KG)*2.2
		print("Weight in pounds:", round(weight_P,2))
		break
	

