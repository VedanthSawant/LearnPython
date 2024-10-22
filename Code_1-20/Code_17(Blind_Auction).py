# Write a code for blind auction.
# User need to type their name and bid amount. Next bidder will not ne able to see previous bids. At the end of auction
# highest bidder wins the auction

import MyModule
print(MyModule.hammer_logo)
continue_YN = True
auction_dict = {}
max_value = 0
bidder_name = ""
print("Welcome to the secret auction program")

while continue_YN:
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    auction_dict[name] = bid
    continue_YN = input("Are there any other bidders? Type 'YES' or 'NO'.\n")
    if continue_YN.lower() == 'yes':
        continue_YN = True
    else:
        continue_YN = False
    print("\n"*100)
for key in auction_dict:
    if auction_dict[key] > max_value:
        max_value = auction_dict[key]
        bidder_name = key
print(f"The winner is {bidder_name} with a bid of ${max_value}")
