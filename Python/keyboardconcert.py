# 726th Kattis, A Solution To The Problem: https://open.kattis.com/problems/keyboardconcert

''' General Solution: Greedy Algorithm with a hashmap
    Read in the notes and the instruments that can play certain nodes (hashmap for instruments).
    Try to move as much forward as possible, i.e, choosing the instrument that moves us forward the most.
    At the end, output the index -1 (to account for the very first choice of an instrument). 
'''


n,m = list(map(int,input().split()))
instrument_list = []
for _ in range(n):
    notes = input().split()
    new_map = {}
    for i in range(1, int(notes[0])+1):
        new_map[int(notes[i])] = True
    instrument_list.append(new_map)

note_list = list(map(int,input().split()))
index = 0
counter = 0
n = len(note_list)
while index < n:
    best_index = index

    for instrument in instrument_list:
        internal_index = index
        while internal_index < n and note_list[internal_index] in instrument:
            internal_index += 1
        if internal_index > best_index:
            best_index = internal_index

    counter += 1
    index = best_index
    #print(index)
print(counter-1)
