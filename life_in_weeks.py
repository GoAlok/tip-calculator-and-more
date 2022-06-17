
# Life in Week
print("----------- LIFE IN WEEK -----------")

# step 1 - get user current age
current_age = int(input("What's your age(in years): "))
# step 2 - calculate how many days, weeks, months left if average maximum age is __ years
avg_age = int(input("What is average age in your region(in years): "))
days_left =  (avg_age - current_age) * 365
weeks_left = (avg_age - current_age) * 52
months_left = (avg_age - current_age) * 12
# step 3 - Print the result
msg = (f"You have left total of {months_left} months left OR {weeks_left} \
weeks left OR {days_left} days left. So enjoy your life as much as you can. ")

print(msg)