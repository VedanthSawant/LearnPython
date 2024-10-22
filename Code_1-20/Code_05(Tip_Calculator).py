# Write a program to calculate how much each person should pay at restaurant
print("Welcome to tip calculator")
total_bill = float(input("What was the total bill? $"))
total_tip = float(input("How much tip would you ike to give? 10, 12 or 15? "))
total_ppl = float(input("How many people to split the bill? "))
bill_after_tip = total_bill + ((total_tip / 100) * total_bill)
after_split = bill_after_tip / total_ppl
print(f"Each person should pay: ${round(after_split, 2)}")