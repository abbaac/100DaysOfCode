from replit import clear
from art import logo

bids = {}
resume = True

def add_bid(bidder, amount):
    bids[bidder] = amount
    
print(logo)
print("Welcome to the Silent Auction!\n")
while resume == True:
    name = input("What is your first name: ")
    bid = int(input("How much do you want to bid: $"))
    add_bid(name, bid)

    choice = input("Are there any other bidders? (y/n): ").lower()

    if choice == "y":
        resume = True
        clear()
    elif choice == "n":
        resume = False
        clear()
        bidder = ""
        maximum = 0 
        for i in bids:
            if bids[i] > maximum:
                bidder = i
                maximum = bids[i]

        print(f"The highest bidder is {bidder} with {maximum}")
    




