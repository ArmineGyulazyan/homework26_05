inp_year = int(input("Please enter the year: "))
count = 0
for leap_year in range(1600,inp_year+1):
	if (leap_year % 4 == 0 and leap_year % 100 != 0) or leap_year % 400==0:
		count+=1	
		print(leap_year)

print("the number of leap years is ",count)	