import itertools

possibleValues = []
x = 0
reg1 = 0
reg2 = 0

def Reg1EqualsX():
    global x, reg1
    reg1 = x

#Has to execute x2 times
def Reg2EqualsX():
    global x, reg2
    reg2 = x

def XEqeualsReg1():
    global x, reg1
    x = reg1

#Has to execute x2 times
def XEqeualsReg2():
    global x, reg2
    x = reg2

def RegPlus1():
    global reg2
    reg2 = reg2 + 1

def RegPlus2():
    global reg1
    reg1 = reg1 + 2

def RegPlus3():
    global reg2
    reg2 = reg2 + 3

def CompleteArray():
    global x, reg1, reg2
    if x not in possibleValues:
        possibleValues.append(x)
    x = 0
    reg1 = 0
    reg2 = 0

listOfInstructions = [Reg1EqualsX, Reg2EqualsX, RegPlus1, XEqeualsReg2, Reg2EqualsX, RegPlus3, XEqeualsReg2, RegPlus2, XEqeualsReg1]
possibleOrders = list(itertools.permutations(listOfInstructions))
for possibleOrder in possibleOrders:
    for instruction in possibleOrder:
        instruction()
    CompleteArray()
    print(possibleValues)
print(possibleValues)