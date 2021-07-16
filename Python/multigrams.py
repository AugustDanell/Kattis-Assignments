def is_anagram(w1,w2):
    w1.sort()
    w2.sort()

    return w1 == w2

def one_letter_only(s):
    start = s[0]
    for i in range(1,len(s),1):
        if(s[i] != start):
            return False
    return True

# TODO: Optimate
def divisors(n):
    divisor_list = []
    for i in range(1,(n//2)+1, 1):
        if(n%i == 0):
            divisor_list.append(i)

    return divisor_list

data = input()
if(one_letter_only(data)):
    print(data[0])
else:
    length_data = len(data)
    partitions = divisors(length_data)
    length_part = len(partitions)

    all_anagrams = False
    anagram_candidate = ""

    for d in partitions:                    
        div_length = length_data // d
        all_anagrams = True
        w_first = data[:d]

        for i in range(div_length-1):
            w1 = data[i*d:(i+1)*d]
            w2 = data[(i+1)*d:(i+2)*d]
            anagram_candidate = w_first

            if(not is_anagram(list(w1),list(w2))):
                all_anagrams = False
                break

        if(all_anagrams):
            break

    if(all_anagrams):
        print(anagram_candidate)
    else:
        print(-1)
