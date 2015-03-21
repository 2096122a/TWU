##Goody Pack – Contains health, bullets and upgrades.
##A list containing the possibilities may be easiest.
##Have :
##Health (random int 1-3) –A, 
##Ammo(random int 1-3) –B
##Gun Upgrade – C
##Melee Upgrade –D.
##The list would be the power set of A, B, C, D.
##Once an upgrade is acquired, the relevant option would be removed.
##For example, once the gun upgrade is obtained, the list becomes the power set of A, B, D.
##A goody pack should not be on every map tile.
##I suggest a 50% chance, maybe less. Simple call a random integer, and if the int is even,
##a goody pack is created on the tile, and picked up automatically by the player.
##These goody packs are never replenished, and only appear when the tile is uncovered, unlike zombies.

import random
min = 1
max = 3
health = 'health'
ammo = 'ammo'
gunUpg = 'gun upgrade'
melUpg = 'melee upgrade'
itemset = [health,ammo,gunUpg,melUpg]

def powerset(itemset):
    #returns subsets of intial itemset
    if len(itemset) <= 1:
        yield itemset
        yield []
    else:
        for item in powerset(itemset[1:]):
            yield [itemset[0]]+item
            yield item
            
r = [x for x in powerset(itemset)]
r.sort()

#while (new tile):
if random.randint(0,100) < 50: #sets 50% chance
    goodiebag = random.choice(r)
    if goodiebag == []:
        print "No upgrades on this tile."
    else:
        print goodiebag
        if 'gun upgrade' in goodiebag:
            if 'melee upgrade' in goodiebag:
                itemset = [health,ammo]
                r = [x for x in powerset(itemset)]
                r.sort()
                itemset = r
                print itemset
            else:
                itemset = [health,ammo,melUpg]
                r = [x for x in powerset(itemset)]
                r.sort()
                itemset = r
                print itemset
        elif 'melee upgrade' in goodiebag:
            itemset = [health,ammo,gunUpg]
            r = [x for x in powerset(itemset)]
            r.sort()
            itemset = r
            print itemset
        if 'health' in goodiebag:
            #sets health for udpating
            health = random.randint(min, max)
            print health
        if 'ammo' in goodiebag:
            #sets ammo for updating
            ammo = random.randint(min, max)
            print ammo
else:
    print "No upgrades on this tile."













