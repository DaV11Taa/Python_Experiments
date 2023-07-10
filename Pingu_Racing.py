def limit(SPEED):
    _SPEED = int(SPEED)
    if _SPEED > 128:
        return 128
    elif _SPEED < 0:
        return 0
    else:
        return _SPEED


# TO MAKE INPUTS
POSA = int(input("Alan Starting position: "))
POSB = int(input("Bjarne starting position: "))
Tduraction = int(input("Race duration: "))
while True:
    if Tduraction < 0:
        Tduraction = int(input("Please do not enter a negative number: "))
    else:
        break
# LOGIC AND CONDITIONS
SPEA = 0
SPEB = 0
# FIRST HALF
for i in range(0, int(Tduraction / 2)):
    print(f"t = {str(i)}")
    if POSA % 10 == 4 or POSA % 10 == -4:
        SPEA = SPEA / 2
        SPEA = int(SPEA) + 1
    else:
        SPEA = SPEA + 7
    SPEA = limit(SPEA)
    POSA = POSA + SPEA
    print(f"Alan Position = {POSA}; speed = {SPEA}")
    if POSB % 13 == 0:
        SPEB = SPEB * 2
        SPEB = SPEB + 1
    else:
        SPEB = SPEB + 3
    SPEB = limit(SPEB)
    POSB = POSB + SPEB
    print(f"Bjarne position = {POSB}; speed = {SPEB}")
# SECOND HALF
for i in range(int(Tduraction / 2), Tduraction):
    print(f"t = {str(i)}")
    if i == int(Tduraction * 3 / 5) or i == int(Tduraction * 4 / 5):
        SPEA = int(SPEA / 4)
    else:
        SPEA = SPEA + 1
    SPEA = limit(SPEA)
    POSA = POSA + SPEA
    print(f"Alan Position = {POSA}; speed = {SPEA}")
    if i >= Tduraction - 13:
        SPEB = int(SPEB / 2)
    else:
        SPEB = SPEB + 1
    SPEB = limit(SPEB)
    POSB = POSB + SPEB
    print(f"Bjarne position = {POSB}; speed = {SPEB}")
# TO PRINT OUT THE RESULT
if POSA < POSB:
    print("Bjarne wins!")
elif POSA > POSB:
    print("Alan wins!")
else:
    print("Draw!")
# THE END
