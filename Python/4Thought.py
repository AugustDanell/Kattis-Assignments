def expressionParsing(s):
    l = s.split()
    operations = []
    operands = []
    for element in l:
        if element in ["+", "-", "*", "/"]:
            operations.append(element)
        else:
            operands.append(int(element))

    # Level one.
    index = 0
    while index < len(operations):
        if operations[index] == "*":
            operands[index] = operands[index] * operands[index +1]
            operands.pop(index+1)
            operations.pop(index)
        elif operations[index] == "/":
            operands[index] = operands[index] // operands[index +1]
            operands.pop(index+1)
            operations.pop(index)
        else:
            index += 1

    # Level Two:
    while len(operations) > 0:
        operation = operations.pop(0)
        if operation == "+":
            operands[0] = operands[0] + operands[1]
        elif operation == "-":
            operands[0] = operands[0] - operands[1]

        operands.pop(1)

    return int(operands[0])

def tryAllFours(sumToFind):
    mathematicalOperations = ["+", "-", "*", "/"]
    for firstOperation in mathematicalOperations:
        for secondOperation in mathematicalOperations:
            for thirdOperation in mathematicalOperations:
                inString = "4 {0} 4 {1} 4 {2} 4".format(firstOperation, secondOperation, thirdOperation)
                ans = expressionParsing(inString)

                if sumToFind == ans:
                    return inString
    return None

testing = False
if testing:
    assert expressionParsing("4 + 4 + 4 / 4") == 9
    assert expressionParsing("4 * 4 - 4 * 4") == 0
    assert expressionParsing("4 + 4 - 4 / 4") == 7
    assert expressionParsing("4 * 4 + 4 + 4") == 24

testCases = int(input())
for test in range(testCases):
    s = int(input())
    ans = tryAllFours(s)

    if ans == None:
        print("no solution")
    else:
        print("{0} = {1}".format(ans, s))
