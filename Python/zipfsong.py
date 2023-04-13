# A quick, straight forward solution to: https://open.kattis.com/problems/zipfsong
if __name__ == "__main__":
    n,m = list(map(int,input().split()))
    data = input().split()
    first_score = int(data[0])
    first_name = data[1]

    q_list = [[first_name, first_score]]
    for i in range(1, n):
        data = input().split()
        score = int(data[0])
        name = data[1]
        multiplier = (i+1)
        q_score = multiplier * score
        q_list.append([name, q_score])

    f = lambda element: element[1]
    q_list = sorted(q_list, key = f, reverse= True)
    for i in range(m):
        element = q_list[i]
        print(element[0])
