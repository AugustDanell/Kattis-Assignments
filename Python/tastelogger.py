# Just have a map for every key sound and process the out string accordingly:
N = int(input())
shift = False
caps = False
letterMap = {"clank":"a",
             "bong": "b",
             "click": "c",
             "tap": "d",
             "poing": "e",
             "clonk": "f",
             "clack": "g",
             "ping": "h",
             "tip": "i",
             "cloing":"j",
             "tic": "k",
             "cling": "l",
             "bing": "m",
             "pong": "n",
             "clang": "o",
             "pang": "p",
             "clong": "q",
             "tac": "r",
             "boing": "s",
             "boink": "t",
             "cloink": "u",
             "rattle": "v",
             "clock": "w",
             "toc": "x",
             "clink": "y",
             "tuc": "z",
             "whack": " "}

out = ""
for i in range(N):
    line = input()
    if(line == "dink"):
        shift = True
    elif (line == "thumb"):
        shift = False
    elif line == "bump":
        caps = not caps
    elif line == "pop":
        if len(out) > 0:
            out = out[:-1]

    else:
        letter = letterMap[line]
        if (shift or caps) and not (shift and caps):
            letter = letter.upper()

        out += letter

print(out)
