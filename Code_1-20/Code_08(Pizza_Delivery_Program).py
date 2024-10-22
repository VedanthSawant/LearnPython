# Write a program for pizza deliveries.
# Small: $15, Medium: $20, Large: $25
# Pepperoni on small: extra $2, pepperoni on medium and large: extra $3
# For cheese: extra $1

print("Welcome to python pizza deliveries.")
pizza_price = 0
pizza_size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Type Y for YES & N for NO: ")
cheese = input("Do you want extra cheese on your pizza? type Y for YES & N for NO: ")

if pizza_size.lower() == "s":
    pizza_price += 15
    if pepperoni.lower() == "y":
        pizza_price += 2
elif pizza_size.lower() == "m":
    pizza_price += 20
    if pepperoni.lower() == "y":
        pizza_price += 3
else:
    pizza_price += 25
    if pepperoni.lower() == "y":
        pizza_price += 3

if cheese.lower() == "y":
    pizza_price += 1

print(f"Your pizza order cost is ${pizza_price}")

