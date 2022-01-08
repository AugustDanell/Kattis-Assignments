'''
    For this problem we divide it up into two cases, a simple case and a general case.
    
    Simple case: In the simple case the number of teams are divided by the number of rooms and we just output the quotient of teams / rooms for all the rooms.
    General case: In the general case we extract a number of remainders and we iterate through the remainders first. When that is done we move on to the simple case.
'''

rooms = int(input())
teams = int(input())

# Simple case: When number of teams divided by number of rooms:
if(teams % rooms == 0):
    for i in range (rooms):
        print((teams//rooms)*"*")
else:
    # General case:
    remainders = teams % rooms
    for i in range(remainders):
        print(((teams // rooms) + 1) * "*")
    for i in range(rooms - remainders):
        print((teams//rooms)*"*")
