drinks = int(input())
drink = input()

while(not drinks == 0):
    if(drinks == 1):
        print("1 bottle of %s on the wall, 1 bottle of %s." %(drink, drink))
        print("Take it down, pass it around, no more bottles of %s." % (drink))
    elif(drinks == 2):
        print("%d bottles of %s on the wall, %d bottles of %s."%(drinks,drink,drinks,drink))
        print("Take one down, pass it around, %d bottle of %s on the wall." %(drinks-1, drink))
        print()
    else:
        print("%d bottles of %s on the wall, %d bottles of %s."%(drinks,drink,drinks,drink))
        print("Take one down, pass it around, %d bottles of %s on the wall." %(drinks-1, drink))
        print()

    drinks = drinks - 1