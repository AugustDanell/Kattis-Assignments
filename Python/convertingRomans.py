# Problem: https://open.kattis.com/problems/convertingromans

if __name__ == "__main__":

    # 1. Init a mapping from roman numerals -> decimal and read in how many N texts we need:
    N = int(input())
    romanMapping = {
                    'I' : 1,
                    'V' : 5,
                    'X' : 10,
                    'L' : 50,
                    'C' : 100,
                    'D' : 500,
                    'M' : 1000,
                    }

    # 2. Iterate over N, and read in a text at a time
    for _ in range(N):

        # 3. For each text, init the largest occured number as -1 and the total sum as 0:
        largestOccuredDigit = -1
        text = list(input())
        totalSum = 0
        
        # 4. Iterate backwards from the text:
        for c in text[::-1]:
            number = romanMapping[c]
            
            # 5. If a roman numeral has had a larger occurance, negate the current one:
            if(largestOccuredDigit > number):
                totalSum -= number
                
            # 6. Else just add it and update the largest occured counter:
            else:
                largestOccuredDigit = number
                totalSum += number
        
        # 7. Print the total sum:
        print(totalSum)
