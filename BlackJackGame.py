# Week 3 Stretch Exercise
# FUN PRACTICE
# https://edabit.com/challenge/hYiCzkLBBQSeF8fKF
# Black Jack
deck = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
import random
max_cards_in_deal = 5
# for now assume this will NOT change, but will want to change it in the future

rules = input("Welcome to practice counting cards! This is legal to do in casinos if you count in your head, but they can kick you out for doing it. Do you want a refresher on the rules? Type Y for yes: ")
if rules == "Y":
    print("Cards that are low cards (2-6) increase the count by one because that means larger cards are still in the deck. The higher the count the more you want to bet! The cards in the middle (7-9) can be ignored. They do nothing to the count. The cards at the top (10-A) lower the count by one. The lower the count the less you want to bet, maybe just the table minimum.")
else:
    print("Awesome, let's get you a deal of cards!")

list_of_deal = []
deal_count = 0
while deal_count < max_cards_in_deal:
    random_card = random.choice(deck)
    list_of_deal.append(random_card)
    deal_count = deal_count + 1
print(list_of_deal)
guess = int(input("what is your guess of the count? "))
hints = input("do you want to see how we determine the count? Type Y for yes? ")

# check the max_cards_in_deal is how many cards you got back? YES
# count_math = len(list_of_deal)
# only need this if changing the max_cards_in_deal in the future

# create a copy of list_of_deal so you can mess with it
manip_deal = list_of_deal
manip_count = 0
math = 0

while manip_count < max_cards_in_deal:
    if (manip_deal[0] == '2') or (manip_deal[0] == '3') or (manip_deal[0] == '4') or (manip_deal[0] == '5') or (manip_deal[0] == '6'):
        if (hints == "Y"):
            print("add one")
            math = math + 1
        else:
            math = math + 1
    elif (manip_deal[0] == '10') or (manip_deal[0] == 'J') or (manip_deal[0] == 'Q') or (manip_deal[0] == 'K') or (manip_deal[0] == 'A'):
        if (hints == "Y"):
            print("subtract one")
            math = math - 1
        else:
            math = math -1
    else:
        if (hints == "Y"):
            print("no change to count")
        else:
            math = math
    manip_deal.remove(manip_deal[0])
    manip_count = manip_count + 1

if guess == math:
    print("Congrats! You are correct. The count is " + str(math) + ".")
else:
    print("Sorry you are incorrect. The correct count is " + str(math) + ". You can try again and see how the count changes with each card. Type Y for yes when asked.")

# printing original list shows something is wrong here, because it is empty
# I thought by creating manip_deal I could delete it piece by piece, without effecting the original list
print(list_of_deal)
