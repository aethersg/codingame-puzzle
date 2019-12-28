# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
p1, p2 = [], []
card_value = {
    "2": 1,
    "3": 2,
    "4": 3,
    "5": 4,
    "6": 5,
    "7": 6,
    "8": 7,
    "9": 8,
    "1": 9,
    "J": 10,
    "Q": 11,
    "K": 12,
    "A": 13
}

n = int(input())  # the number of cards for player 1
for i in range(n):
    cardp_1 = input()  # the n cards of player 1
    p1.append(cardp_1)
m = int(input())  # the number of cards for player 2
for i in range(m):
    cardp_2 = input()  # the m cards of player 2
    p2.append(cardp_2)
# Write an action using print
# To debug: print >> sys.stderr, "Debug messages..."
war1, war2 = [], []

count = 0

while p1 and p2:
    card1 = p1.pop(0)
    card2 = p2.pop(0)
    if card_value[card1[0]] > card_value[card2[0]]:
        war1.append(card1)
        war2.append(card2)
        p1.extend(war1)
        p1.extend(war2)
        war1, war2 = [], []
        count += 1
    elif card_value[card1[0]] < card_value[card2[0]]:
        war1.append(card1)
        war2.append(card2)
        p2.extend(war1)
        p2.extend(war2)
        war1, war2 = [], []
        count += 1
    else:
        war1.append(card1)
        war2.append(card2)

        for x in range(3):
            if p1 and p2:
                card1 = p1.pop(0)
                card2 = p2.pop(0)
                war1.append(card1)
                war2.append(card2)
            else:
                p1 = []
                p2 = []
                break
if len(p1) == 0:
    if len(p2) == 0:
        print("PAT")
    else:
        print("2 %d" % count)
else:
    if len(p2) == 0:
        print("1 %d" % count)
