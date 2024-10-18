# Create a function called life_in_weeks() using maths and f-Strings that tells us how many weeks we have left,
# if we live until 90 years old.
# It will take your current age as the input and output a message with our time left in this format:
# You have x weeks left.
# Where x is replaced with the actual calculated number of weeks the input age has left until age 90.

def life_in_weeks(age):
    week_in_year = 52
    years_left = 90 - age
    weeks_left = years_left * week_in_year
    return weeks_left


age = int(input("Enter your age: "))
life_in_weeks = life_in_weeks(age)
print(f"You have {life_in_weeks} weeks left.")
