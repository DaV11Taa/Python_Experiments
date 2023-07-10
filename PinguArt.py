# TO CHECK NUMBER IF IT CONTAINS 8 NUMBERS
def check(code):
    _code = str(code)
    if len(_code) < 8:
        while True:
            _code = _code + "0"
            if len(_code) == 8:
                break
    return _code


# CONVERTING NUMBER TO CODE
def Convent(code):
    _code = str(code)
    _code = _code.replace("0", " ")
    _code = _code.replace("1", "-")
    _code = _code.replace("2", "~")
    _code = _code.replace("3", "P")
    return _code


# TO PRINT COLUMNS
def PrintColumn(codeF, codeS):
    _codeF = str(codeF)
    _codeS = str(codeS)
    print("|", end="")
    z = 7
    while z >= 0:
        print(_codeF[z], end="")
        z = z - 1
    z = 7
    while z >= 0:
        print(_codeS[z], end="")
        z = z - 1
    print("|")


# THE MAIN PROGRAM
column = ["0", "0", "0", "0", "0", "0", "0", "0"]
for i in range(0, 8):
    column[i] = input("Please enter a Pingu Art number: ")
    column[i] = check(column[i])
    column[i] = Convent(column[i])
# OUTPUT INTERFACE
k = 0
print("+---[PinguArt]---+")
while True:
    PrintColumn(column[k], column[k + 1])
    k = k + 2
    if k == 8:
        break
print("+----------------+")
