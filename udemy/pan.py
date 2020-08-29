import random
from collections import Counter

playerFirst = []
playerSecond = []



cardsList = ["9", "9", "9", "9",
            "10", "10", "10", "10",
            "Jack", "Jack", "Jack", "Jack",
            "Queen", "Queen", "Queen", "Queen",
            "King", "King", "King", "King",
            "Ace",  "Ace",  "Ace",  "Ace",
            "Joker", "Joker"]

random.shuffle(cardsList)

for x in range(5):
    playerFirst.append(cardsList.pop())
    playerSecond.append(cardsList.pop())

print(playerSecond)
print(playerFirst)
print(Counter(cardsList))

