def quiz():
    points = 0
    print('Which operator has higher precedence in the following list?\na) % (Modulus)\nb) & (BitWise AND)\nc) ** (Exponent)\nd) > (Comparison)')
    answer = input('Chose your answer: a,b,c or d ->\n')
    if answer.lower() == 'c':
        points = points + 1
    return points

if __name__ == '__main__':
    if quiz() == 1:
        print('congrats you win the game!')
        print('go on other turn!')
    else:
        print('loosseeerr!')