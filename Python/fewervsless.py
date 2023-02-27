cWords = {"number of": True,
          "fewest":    True,
          "more":      True,
          "fewer":     True,
          "many":      True,
          "few":       True,
          "most":      True}

mWords = {"amount of": True,
          "most":      True,
          "least":     True,
          "more":      True,
          "less":      True,
          "much":      True,
          "little":    True}

words,queries = list(map(int, input().split()))

for i in range(words):
    data = input().split()
    if(data[1] == "c"):
        cWords[data[0]] = True
    else:
        mWords[data[0]] = True

for i in range(queries):
    data = input().split()

    word = data[-1]
    quantifier = ""
    if data[0] == "amount":
        quantifier = "amount of"
    elif data[0] == "number":
        quantifier = "number of"
    else:
        quantifier = data[0]

    if mWords.__contains__(quantifier) and mWords.__contains__(word):
        print("Correct!")
    elif cWords.__contains__(quantifier) and cWords.__contains__(word):
        print("Correct!")
    else:
        print("Not on my watch!")
