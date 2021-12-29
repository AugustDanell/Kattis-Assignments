threshholds = list(map(int, input().split()))
score = int(input())
current_grade_mark = 0
for i in reversed(threshholds):
    if(score >= i):
        current_grade_mark += 1

dictionary = {
    0 : 'F',
    1 : 'E',
    2 : 'D',
    3 : 'C',
    4 : 'B',
    5 : 'A'
}

print('{0}'.format(dictionary[current_grade_mark]))
