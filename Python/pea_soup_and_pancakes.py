cases = int(input())
found = False
found_name = ""

for t in range(cases):
    items = int(input())
    name = input()
    menu = []
    for i in range(items):
        menu.append(input())

    if(not found):
        if("pea soup" in menu and "pancakes" in menu):
            found = True
            found_name = name

if(found_name == ""):
    print("Anywhere is fine I guess")
else:
    print(found_name)
