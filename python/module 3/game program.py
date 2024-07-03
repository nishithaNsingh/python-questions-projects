
from numpy import random
sticks=21
while sticks>0:
    print("Choose a stick ")
    player=random.randint(1,4)
    print("comp chooses: ",5-player)
    sticks-=5
    if sticks==1:
        print("player looses")
        break
