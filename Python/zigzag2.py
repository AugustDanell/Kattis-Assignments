# A solution to the problem: https://open.kattis.com/problems/zigzag2

def largest_zig_zag(numbers, asc):
    zigzags = []

    # 1. Read in number after number:
    for element in numbers:

        # 2. If we have appended no numbers we append the first:
        if len(zigzags) == 0:
            zigzags.append(element)
        else:
            
            # 3. Else we look if we are in our ascending or descending order:
            if asc:

                # 4. What we can do is to update our last value if we cannot append a value according to our sort scheme (ascending / descindg):
                if element < zigzags[-1]:
                    zigzags[-1] = element
                elif element > zigzags[-1]:
                    asc = False
                    zigzags.append(element)
            else:
                if element > zigzags[-1]:
                    zigzags[-1] = element
                elif element < zigzags[-1]:
                    asc = True
                    zigzags.append(element)
                    
    # 5. Return the best zig zag available, where asc is the parametric flag that decides which sorting scheme to start with:
    return zigzags

if __name__ == "__main__":

    # 1. Do input and fill a list of numbers:
    n = int(input())
    numbers = []
    for _ in range(n):
        numbers.append(int(input()))
    
    # 2. Output the max result between starting either ascendingly or descendingly and passing ditto to the function largest_zig_zag()
    print(max(len(largest_zig_zag(numbers, True)), len(largest_zig_zag(numbers, False))))
