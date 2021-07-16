def calculate(l,prev_op):
    a, op, b = l
    a,b = int(a), int(b)

    if(op == "*"):
        return (a*b)**2

    if(op == "/"):
        return (a+1)//2

    if(op == "+"):
        return a+b - prev_op

    if(op == "-"):
        return (a-b)*prev_op

operations = int(input())
prev_op = 1

for i in range(operations):
    prev_op = calculate(input().split(), prev_op)
    print(prev_op)
