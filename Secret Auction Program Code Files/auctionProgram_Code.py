from auctionArt import logo
print(logo)
print("Welcome to the Secret Auction Bid Program. Designed by Mahmood Khan...")

# Function for comparing bids and finding the highest bidder
def comparing_bids(bidding_Data):
    highestBid = 0
    winner = ""
    for bidder in bidding_Data:
        biddingAmount = bidding_Data[bidder]
        if biddingAmount > highestBid:
            highestBid = biddingAmount
            winner = bidder
    print(f"The Highest Bidder in the Auction was: {winner}.")
    print(f"Their bid was: {highestBid}")

bids = {}
continue_bidding = True

# Main bidding loop
while continue_bidding:
    bidderName = input("What's your name Mr/Mrs? ")
    bidderValue = int(input(f"Enter your bid Mr/Mrs {bidderName}: "))  # Convert input to integer

    # Save the bid in the dictionary
    bids[bidderName] = bidderValue

    # Ask if there are more bidders
    should_continue = input("Are there any new bidders that need to participate? (yes/no)? ").lower()
    if should_continue == "no":
        continue_bidding = False
        comparing_bids(bids)
    elif should_continue == "yes":
        print("\n" * 20)
    else:
        break