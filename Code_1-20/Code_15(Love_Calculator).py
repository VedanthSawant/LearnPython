# 💪 This is a difficult challenge! 💪
# You are going to write a function called calculate_love_score() that tests the compatibility between two names.
# To work out the love score between two people:
# 1. Take both people's names and check for the number of times the letters in the word TRUE occurs.
# 2. Then check for the number of times the letters in the word LOVE occurs.
# 3. Then combine these numbers to make a 2 digit number and print it out.
# e.g.
# name1 = "Angela Yu" name2 = "Jack Bauer"
# T occurs 0 times
# R occurs 1 time
# U occurs 2 times
# E occurs 2 times
# Total = 5
# L occurs 1 time
# O occurs 0 times
# V occurs 0 times
# E occurs 2 times
# Total = 3
# Love Score = 53

# in the below code, count function is used to count the number of alphabet in the give word
def calculate_love_score(name_one, name_two):
    final_name = name_one.lower() + name_two.lower()
    t_count = final_name.count("t")
    r_count = final_name.count("r")
    u_count = final_name.count("u")
    e_count = final_name.count("e")
    true_count = t_count + r_count + u_count + e_count
    l_count = final_name.count("l")
    o_count = final_name.count("o")
    v_count = final_name.count("v")
    e_count = final_name.count("e")
    love_count = l_count + o_count + v_count + e_count
    final_count = str(true_count) + str(love_count)
    return final_count

one_name = input("Enter boy's name: ")
two_name = input("Enter girl's name: ")
love_score = calculate_love_score(one_name, two_name)
print(f"Love Score is {love_score}")
