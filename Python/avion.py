# Avion problem

rows = ""
for i in range (5):
    s = (input())
    for j in range(len(s)-2):
         if(s[j] == 'F' and s[j+1] == 'B' and s[j+2] == 'I'):
             rows += " " + (i+1).__str__()

rows = rows[1:]
if(rows == ""):
    print("HE GOT AWAY!")
else:
    print(rows)