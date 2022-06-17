
# build the TIP CALCULATOR

print("--------- TIP CALCULATOR ---------")

# Task - Get total bill amount from user and how much tip they want to give on 
# that amount and in how many equal parts they want to divide that amount.
# rupee sign  = ₹

# calculate percentage of any number : 
# i.e. 12% of 138 ==> 138*12/100

# Getting Input
bill = float(input("What is your total bill(₹): "))
tip = float(input("What is the percentage of tip you want to give 10, 12 or 15: "))
split_into = int(input("In how many person you want to split the bill into: "))

# Calculations
total_bill = round(bill + ((bill * tip)/100), 2)
per_person = round((total_bill / split_into) , 2)

# Result
msg = f"Your total amount is ₹{total_bill}, and each person have to pay ₹{per_person}"
print(msg)
