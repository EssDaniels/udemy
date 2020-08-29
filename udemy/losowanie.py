import random
from collections import Counter

def will_weapon_hit(weaponChanceToHitPercentage):
    isHitChance = random.uniform(0, 100)
    if (isHitChance < weaponChanceToHitPercentage):
        return "hit"
    else:
        return "not hit"


x = 0
listHit = []

while x < 100:
    x = x + 1
    listHit.append(will_weapon_hit(50))

dictionaryHit = Counter(listHit)

print(dictionaryHit)



