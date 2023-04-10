# A solution to the problem: https://open.kattis.com/problems/fbiuniversal

def get_numbers():
    return list("0123456789ACDEFHJKLMNPRTVWX")
def replace_all(s):
    s.replace("B", "8")
    s.replace("G", "C")
    s.replace("I", "1")
    s.replace("O", "0")
    s.replace("Q", "0")
    s.replace("S", "5")
    s.replace("U", "V")
    s.replace("Y", "V")
    s.replace("Z", "2")
    return s
def decimal_sum(num_str):
    sum_ = 0
    letters = get_numbers()
    power = 0
    for letter in num_str[::-1]:
        sum_ += letters.index(letter)*(27**power)
        power +=1

    return sum_
def calculate_check_sum(s):
    check_sum = 0
    letters = get_numbers()
    check_sum += 2*letters.index(s[0])
    check_sum += 4*letters.index(s[1])
    check_sum += 5*letters.index(s[2])
    check_sum += 7*letters.index(s[3])
    check_sum += 8*letters.index(s[4])
    check_sum += 10*letters.index(s[5])
    check_sum += 11*letters.index(s[6])
    check_sum += 13*letters.index(s[7])
    return check_sum%27

if __name__ == "__main__":
    testcases = int(input())
    for _ in range(testcases):
        dataset, num = input().split()
        rep_num = list(replace_all(num))
        check_sum = calculate_check_sum(rep_num)
        check_digit = get_numbers().index(rep_num.pop())
        decimal_ = decimal_sum(rep_num)

        if check_digit == check_sum:
            print(dataset, decimal_)
        else:
            print(dataset, "Invalid")
