# A solution to the simple problem: https://open.kattis.com/problems/offworldrecords
'''
  General Solution:
  1. Set the initial previous record and the current record.
  2. Iterate over any new ones and update if needed, incrementing the count as we go.
  3. Print the count.
'''

n,c,p = list(map(int,input().split()))
previous = p
current = c
count = 0

for _ in range(n):
    newData = int(input())
    if(newData > previous + current):
        previous = current
        current = newData
        count += 1
    
print(count)
