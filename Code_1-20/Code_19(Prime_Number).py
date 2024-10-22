# write a program to check if the number is prime or not

def is_prime(num):
    if num == 2:
        return True
    if num == 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

user_num = int(input("Enter the number: "))
if is_prime(user_num):
    print(f"{user_num} is a prime number.")
else:
    print(f"{user_num} is not a prime number.")