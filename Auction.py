#from replit import clear
#HINT: You can call clear() to clear the output in the console.
name = input('Name: ')
bid = input('Bid: ')
list_of_bids = {}

def biddings(name, bid):
    bidding = {}
    bidding['name'] = name
    bidding['bid'] = bid
    list_of_bids.update(bidding)
    
biddings(name, bid)
print(list_of_bids)
new_person = input("Is there another bidder? ")

while new_person == 'yes':
    name = input('Name: ')
    bid = input('Bid: $')
    biddings(name, bid)
    print(list_of_bids)
    new_person = input("Is there another bidder? ")
    