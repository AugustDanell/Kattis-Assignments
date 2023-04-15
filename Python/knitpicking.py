def get_max_socks(left_socks, right_socks, any_types):
    socks = 0

    for key in any_types.keys():
        if key not in left_socks and key not in right_socks:
            socks += 1

    for key in left_socks.keys():
        if key in right_socks:
            socks += max(left_socks[key], right_socks[key])
        else:
            socks += left_socks[key]

    for key in right_socks.keys():
        if key not in left_socks:
            socks += right_socks[key]

    return socks + 1

if __name__ == "__main__":
    types = int(input())
    possible = False
    left_types = {}
    right_types = {}
    any_types = {}

    for _ in range(types):
        name, sock_type, number = input().split()
        number = int(number)
        if sock_type == "any":
            any_types[name] = number
            if number > 1:
                possible = True

        elif sock_type == "left":
            left_types[name] = number
            if name in right_types:
                possible = True

        elif sock_type == "right":
            right_types[name] = number
            if name in left_types:
                possible = True

    if possible:
        print(get_max_socks(left_types, right_types, any_types))
    else:
        print("impossible")
