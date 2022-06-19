# Musical Scales

def all_in(l1, l2):
    for element in l1:
        if not element in l2:
            return False

    return True

notes = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]
sequence = [2, 2, 1, 2, 2, 2, 1]
d = {}

start = 0
for note in notes:
    l = [notes[start]]
    index = start

    for s in sequence:
        index = (index+s) % len(notes)
        l.append(notes[index])

    d[note] = l
    start += 1

amount_of_notes_played = int(input())
played_notes = list(input().split())
eligble_notes = []

for note in notes:
    if(all_in(played_notes, d[note])):
        eligble_notes.append(note)

if(len(eligble_notes) > 0):
    print(" ".join(eligble_notes))
else:
    print("none")
