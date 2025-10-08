print("Welcome to the secret auction program.")

another_bidder = True

bidders = {
    "name" : [],
    "bids" : []
    }

while(another_bidder):

    bidder_name = input("What is your name?: ")
    bidder_value = int(input("What`s your bid?: "))
    more_bids = input("Are there any other bidders? Type 'yes' or 'no': ").lower()

    bidders["name"].append(bidder_name)
    bidders["bids"].append(bidder_value)

    print("\n" * 28)

    if more_bids == "no":

        higher_value = 0
        winner = ""
        for value in bidders["bids"]:
            if value > higher_value:
                higher_value = value
                winner = bidders["name"][bidders["bids"].index(value)]

        print(f"The winner is {winner} with the bid of ${higher_value}. Congratulations!!")
        print("\n" * 2)
        another_bidder = False