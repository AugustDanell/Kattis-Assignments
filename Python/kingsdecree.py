# A solution to: https://open.kattis.com/problems/kingsdecree

# A function that collects as much money into a "treasury" as possible:
def collect_to_treasury(l, min_l):
    s = 0
    for i in range(len(l)):
        contribution = max(0, l[i]-min_l[i])
        if contribution > 0:
            l[i] -= contribution
            s += contribution
    return s

# A function that finds the smallest item (currently not used):
def find_smallest(l, wealth_map):
    smallest = 0
    for i in range(len(l)):
        if wealth_map.__contains__(l[i]):
            wealth_map[l[i]] += 1
        else:
            wealth_map[l[i]] = 1

        if i == 0:
            smallest = l[0]
        else:
            smallest = min(smallest, l[i])

    return smallest

# A slow distrubtion iteratively based O(n^2), (Time Limit Exceeded):
def mapped_dist(smallest,treasury, wealth_map):
    dist = 0
    while treasury > 0:
        if wealth_map.__contains__(smallest):
            dist += wealth_map[smallest]
        if treasury - dist < 0:
            break
        else:
            treasury -= dist
        smallest +=1
    print(smallest)

# A faster approach. This function is O(n) but it is predicated on cats being sorted, so actually O(n log n):
def sorted_dist(treasury, cats):
    
    # 1. We have a counter for how many cats are the poorest:
    smallest_total = 1
    
    # 2. We iterate over every cat and we are looking at the current cat and the next cat:
    for i in range(0,len(cats)-1):
        current = cats[i]
        next = cats[i+1]
        
        # 3. If the two cats are the same wealth, we increment the counter for the amount of poorest and continue:
        if current == next:
            smallest_total += 1
        else:
            # 4. If this is not the case we calculate the adjustment policy as height (next-current) times width (smallest_total):
            adjustment = (next-current)*smallest_total
            
            # 5. If the treasury can pay for the adjustment we subtract the adjustment, else we return as much as we can adjust:
            if adjustment > treasury:
                return cats[0] + (treasury//smallest_total)
            else:
                treasury -= adjustment
                cats[0] += (next-current)
                smallest_total +=1
    
    # 6. If we have adjusted such that every cat is equal in wealth we return the maximum amount of incrementations to every cat:
    return cats[0] + (treasury//len(cats))

# 0. Read in testcases:
testcases = int(input())
for _ in range(testcases):
  
    # 1. Read in the input:
    n = int(input())
    cats = list(map(int,input().split()))
    min_wealth = list(map(int,input().split()))
    
    # 2. Start with taking as much money as we can in O(n), 
    treasury = collect_to_treasury(cats, min_wealth)
    wealth_map = {}
    
    # 3. Sort cats ascendingly. This is done with a built in Quicksort for O(n log n).
    cats = sorted(cats)

    # 4. Print the result of sorted_dist, this is a distribution scheme based on the data being sorted:
    print(sorted_dist(treasury, cats))
