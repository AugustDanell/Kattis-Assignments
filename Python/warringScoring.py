# 671th Solution: A solution to the problem: https://open.kattis.com/problems/warringscoring

''' Warring Scoring
    Let two functions define the two schemes for deciding the score and then simply see if the equal each other. 
'''

def get_best_diff(l):
    best = [0, 0]
    Yraglac  = 0
    Notnomde = 0
    for name in l:
        if name == "Yraglac":
            Yraglac += 1
        else:
            Notnomde += 1

        if Yraglac > Notnomde:
            local_diff = Yraglac - Notnomde
            if local_diff > best[0]:
                best[0] = local_diff
        elif Notnomde > Yraglac:
            local_diff = Notnomde - Yraglac
            if local_diff > best[1]:
                best[1] = local_diff

    if best[0] > best[1]:
        return "Yraglac"
    elif best[0] == best[1]:
        return "both"
    else:
        return "Notnomde"

def get_best_streak(l):
    streak = [0,0]
    current_streak = 0
    current_name = -1

    for name in l:
        if current_name == name:
            current_streak += 1
        else:
            current_streak = 1
            current_name = name

        if name == "Yraglac" and current_streak > streak[0]:
            streak[0] = current_streak
        elif name == "Notnomde" and current_streak > streak[1]:
            streak[1] = current_streak

    if streak[0] > streak[1]:
        return "Yraglac"
    elif streak[1] > streak[0]:
        return "Notnomde"
    else:
        return "both"


N = int(input())
l = []
for _ in range(N):
    l.append(input())

if get_best_streak(l) == get_best_diff(l):
    print("Agree")
else:
    print("Disagree")
