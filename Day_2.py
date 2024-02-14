print("Welcome to the tip calculator: \n")
name=input("Please, write you name: ")
print("Helo "+name+" mr or mrs")
bill=float(input("What was the total bill? "))
service=int(input("What percentage tip would you like to give? (10, 12, 16 %) "))
people_count=int(input("How many people to split the bill? "))
result=bill*(1+service/100)/people_count
new_result=round(result,2)
print(f" Each person should pay {new_result} dollar")