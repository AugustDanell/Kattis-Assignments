# A solution to the problem: https://open.kattis.com/submissions/10993439
def convert_to_seconds(s):
    return int(s[0])*60 + int(s[1])

def value_function(e, dictionary):
    return dictionary[e][0]*1e10 + int(e)

if __name__ == "__main__":
    l,k,s = list(map(int,input().split()))
    lap_mapping = {}
    for _ in range(l):
        contestant, s = input().split()
        if contestant in lap_mapping:
            lap_mapping[contestant][1] += 1
            lap_mapping[contestant][0] += convert_to_seconds(s.split("."))
        else:
            lap_mapping[contestant] = [convert_to_seconds(s.split(".")), 1]

    f = lambda e : value_function(e, lap_mapping)
    keys = list(sorted(lap_mapping, key = f))
    for key in keys:
        if lap_mapping[key][1] >= k:
            print(key)
