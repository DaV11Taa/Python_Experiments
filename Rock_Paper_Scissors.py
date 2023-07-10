import random

# METHOD TO COMPARE TWO CONDITIONS
def compare(FCOND, SCOND):
    _FCOND = FCOND
    _SCOND = SCOND
    if _SCOND == _FCOND:
        print(f'Second Player: {_SCOND}')
        return 3
    elif _FCOND == "rock" and _SCOND == "scissors":
        print(f'Second Player: {_SCOND}')
        return 1
    elif _FCOND == "scissors" and _SCOND == "paper":
        print(f'Second Player: {_SCOND}')
        return 1
    elif _FCOND == "paper" and _SCOND == "rock":
        print(f'Second Player: {_SCOND}')
        return 1
    else:
        print(f'Second Player: {_SCOND}')
        return 2


def score(SCORE, Result):
    _SCORE = list(SCORE)
    match int(Result):
        case 1:
            _SCORE[0] = _SCORE[0] + 1
            return _SCORE
        case 2:
            _SCORE[1] = _SCORE[1] + 1
            return _SCORE
        case 3:
            return _SCORE


# MAIN PROGRAM
Turnes = ["rock", "paper", "scissors"]
SCORE = [0,0]
while True:
    print("+-------NEW GAME-------+")
    FCOND = input("Player plays: ").lower()
    SCOND = random.choice(Turnes)
    x = compare(FCOND, SCOND)
    print("+------END ROUND-------+")
    match x:
        case 1:
            SCORE = score(SCORE, x)
            print("Result - You win!")
        case 2:
            SCORE = score(SCORE, x)
            print("Result -  You lost!")
        case 3:
            SCORE = score(SCORE, x)
            print("Result - Draw!")

    ask = input("Do you want to start new game or exit? (S/E)\n").lower()
    # TO LOOP THE INPUT
    if ask != "s" and ask != "e":
        while True:
            ask = input("please enter 's' or 'e' S = Start new game , E = Exit.\n").lower()
            if ask != str('e') and ask != str('s'):
                continue
            else:
                break
    # TO CHECK THE INPUT
    if ask == 's':
        continue
    else:
        break
print("+------FINAL SCORE-----+")
print(f' - Your final Score:[{SCORE[0]}:{SCORE[1]}]')
