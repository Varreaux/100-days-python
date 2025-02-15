bidders = {}
while True:
# TODO-1: Ask the user for input
    name = input("What is you name?: ")
    bid = int(input("What is your bid?: "))
    other_bidder = input("Are there any other bidders? Type 'yes' or 'no': \n\t").lower()

# TODO-2: Save data into dictionary {name: price}

    bidders[name] = bid

# TODO-3: Whether if new bids need to be added
    if other_bidder in ['no', 'n']:
        break

    print("\n"*100)

# TODO-4: Compare bids in dictionary

max_bid = 0
max_bidder = ""
for name in bidders:
    if bidders[name]>max_bid:
        max_bid = bidders[name]
        max_bidder = name

print(f"The winner is {max_bidder} with a bid of ${max_bid}")

