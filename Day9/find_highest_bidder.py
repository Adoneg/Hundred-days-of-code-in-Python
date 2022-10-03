



def add_new_bidders (name, bid):
        bidders[name] = bid 

print("Logo")
print("This is an application to find the highest bidder")

bidders =  {}

bidding_finished = False

while not bidding_finished:
        bidder_name = input("What is your name:\n")
        bid = int(input("What is your bid:\n"))

        bidders[bidder_name] = bid
        more_bidders = input("Are there anymore bidders, 'yes' or 'no':\n").lower()
        if more_bidders == 'no':
            bidding_finished = True
      

highest_bid = 0
for key in bidders:
        initial_highest_bid = bidders[key]
        if initial_highest_bid >highest_bid:
            highest_bid = initial_highest_bid 
            name_of_highest_bidder = key
print(f"The highest bid is {highest_bid} which corresponds to {name_of_highest_bidder} ")

