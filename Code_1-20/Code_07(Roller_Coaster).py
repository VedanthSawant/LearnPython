print("Welcome to roller coaster.")
your_bill = 0
your_height = float(input("Enter your height (in cm) : "))
if your_height > 120:
    your_age = int(input("Enter your age : "))
    if your_age < 12:
        your_bill += 5
    elif your_age <= 18:
        your_bill += 7
    else:
        your_bill += 12
    want_photo = input("Do you want a photo to be clicked? Type y for YES and n for NO: ")
    if want_photo == "y":
        your_bill += 3
    print(f"Your final bill for the ride will be ${your_bill}")
else:
    print("Sorry, you cannot ride on roller coaster.")