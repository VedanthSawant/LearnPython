# The body mass index (BMI) is a measure used in medicine to see if someone is underweight or overweight.
# This is the formula used to calculate it:
# bmi is equal to the person's weight divided by the person's height squared.
# Convert this sentence into code on line 6.

# float function is used to convert str to float
# round function rounds up the number to 2 decimal places
# ** operation is used for raised-to(power) calculations

print("Welcome to Body Mass Index(BMI) Calculator")
weight = float(input("Enter your weight (in kg) : "))
height = float(input("Enter your height (in meters) : "))
bmi = round(weight / (height ** 2), 2)
print("Your BMI is " + str(bmi))

# Add some if/elif/else statements to the BMI calculator so that it interprets the BMI values calculated.
# If the bmi is under 18.5 (not including), print out "underweight"
# If the bmi is between 18.5 (including) and 25 (not including), print out "normal weight"
# If the bmi is 25 (including) or over, print out "overweight"

if bmi < 18.5:
    print("Person is underweight.")
elif bmi >= 18.5 and bmi < 25:
    print("Person has normal weight.")
else:
    print("Person is overweight.")
