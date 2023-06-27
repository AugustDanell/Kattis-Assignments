# 732th Kattis. A Solution to the Problem: https://open.kattis.com/problems/raidteams

# 1. Read from input:
N = int(input())
map_a = {}
map_b = {}
map_c = {}

# 2. Read into dictionaries:
for _ in range(N):
    name,a,b,c = input().split()
    map_a[name] = int(a)
    map_b[name] = int(b)
    map_c[name] = int(c)


# 3. Sort on key (lexiographically):
list_a = sorted(map_a.keys(), reverse=True)
list_b = sorted(map_b.keys(), reverse=True)
list_c = sorted(map_c.keys(), reverse=True)

# 4. Sort on value:
sort_on_value_a = lambda x: map_a[x]
sort_on_value_b = lambda x: map_b[x]
sort_on_value_c = lambda x: map_c[x]
sorted_list_a = sorted(list_a, key = sort_on_value_a)
sorted_list_b = sorted(list_b, key = sort_on_value_b)
sorted_list_c = sorted(list_c, key = sort_on_value_c)
taken_players = {}

# 5. Iterate over each team of 3:
while N >= 3:
    person_a = sorted_list_a.pop()
    while person_a in taken_players:
        person_a = sorted_list_a.pop()
    taken_players[person_a] = True

    person_b = sorted_list_b.pop()
    while person_b in taken_players:
        person_b = sorted_list_b.pop()
    taken_players[person_b] = True

    person_c = sorted_list_c.pop()
    while person_c in taken_players:
        person_c = sorted_list_c.pop()
    taken_players[person_c] = True

    # 6. Output the team lexiographically:
    out_list = sorted([person_a, person_b, person_c])
    print(out_list[0], out_list[1], out_list[2])
    N-=3
