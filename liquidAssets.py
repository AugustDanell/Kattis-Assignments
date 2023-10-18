# Problem: https://open.kattis.com/problems/liquidassets

# Function to remove duplicate letters:
def removeDuplicates(word):
    
    # 1. Iterate over every word and check if the next word is the same, if so, dont append, else append:
    newWord = []
    for i in range(len(word) -1):
        if(not word[i] == word[i+1]):
            newWord.append(word[i])
            
    # 2. Append the final letter no matter what:
    newWord.append(word[-1])
    
    # 3. Return as a string every word joined:
    return "".join(newWord)

# Function to remove vowels that are not ending/starting:
def removeIncasedVowels(word):
    
    # 1. Special case, if the word is just one letter, return it, else append the first letter and continue:
    newWord = [word[0]]
    if len(word) == 1:
        return "".join(newWord)
    
    # 2. Iterate in the range [1, N-1] and append only non-vowel letters to the new message:
    vowels = list("aeiou")
    for i in range(1, len(word)-1):
        letter = word[i]
        if letter not in vowels:
            newWord.append(letter)
    
    # 3. Append the last letter no matter what:
    newWord.append(word[-1])
    
    # 4. Return the list joined into a string:
    return "".join(newWord)

# Function to transform a individual word according to the spec:
def reduceWord(word):
    return removeIncasedVowels(removeDuplicates(word))

# Function to transform the input message according to the spec:
def reduceMessage(msg):
    
    # 1. Iterate over every old word and append the reduction to new msg:
    newMsg = []
    words = msg.split()
    for word in words:
        newMsg.append(reduceWord(word))
    
    # 2. Return a join of the new words:
    return " ".join(newMsg)

if __name__ == "__main__":
    
    # 1. Some tests:
    test = True
    if test:
        assert removeDuplicates("coffee") == "cofe"
        assert reduceWord("baked") == "bkd"
        assert reduceMessage("baked potato and beetroot soup") == "bkd ptto and btrt sp"
        assert reduceMessage("dark chocolate coffee cake with a mocha mascarpone frosting") == "drk chclte cfe cke wth a mcha mscrpne frstng"
    
    # 2. Driver code: 
    N = int(input())
    print(reduceMessage(input()))
