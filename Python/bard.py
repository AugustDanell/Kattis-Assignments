def unionOfSongs(dic, vills, l):
    s = []
    for i in range(vills):
        vill = l[i]
        l2 = dic[vill]
        for j in range(len(l2)):
                if(not s.__contains__(l2[j])):
                    s.append(l2[j])

    return s

# Test: unionOfSongs, ok.
#d = {}
#d[1] = [1, 2]
#d[2] = [2, 3]
#d[3] = [3, 4]

#print(unionOfSongs(d, 2, [1,3]))
#print(unionOfSongs(d, 1, [1]))
#print(unionOfSongs(d, 2, [1,2]))

# Verdict: Its a pass
# ------------------------------

#print([1,2,3] + [4])

villagers = int(input())
evenings = int(input())

villSongs = {}
for i in range(villagers):
    villSongs[i+1] = []

# Idea:
# For each row that the Bard is in he gives a new song. All others who are there to listen
# acquire that song. We append that new song to the dictionary for all who are there to listen.
# We then iterate through and append the coalition of songs that the lot know to all present.
# Lastly we output the keys of those villagers whose length of values equals evenings.
# (Output: x, where x is such that: len(villsongs[x]) = evenings)

songs = 0
for i in range(evenings):
    data = input().split()
    vills = int(data[0])

    # Step 1: See if the Bard is here and see who else is here, put them on the list.
    bard = False
    presentList = []
    for j in range(vills):
        if(data[j+1] == "1"):
            bard = True
        else:
            presentList.append(int(data[j+1]))

    # Step 2: Regardless if the bard is here or not everyone present learn the
    # union of all songs

    u = unionOfSongs(villSongs, len(presentList), presentList)

    # Step 2.1: If he is here they also learn the song of the evening
    evening = i + 1
    if(bard):
        songs += 1
        u += [evening]

    # Step 3: They share in each other's songs - All present:
    # Edit this was only if the bard was notthere!

    for p in presentList:
        a = int(p)
        if(not bard):
            villSongs[a] = u
        else:
            villSongs[a] = villSongs[a] + [evening]

#print(villSongs)
print(1)
for i in range(2, villagers+1):
    if(len(villSongs[i]) == songs):
        print(i)

