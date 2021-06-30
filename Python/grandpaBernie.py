import heapq
countries = int(input())
countryMap = {}
sortedMap = {}

for i in range(countries):
    data = input().split()
    country = data[0]
    year = int(data[1])

    if(countryMap.__contains__(country)):
        countryMap[country] += [year]
        #heapq.heappush(countryMap[country],year)
        #heapq.heapify(countryMap[country])
    else:
        countryMap[country] = [year]
        #heapq.heapify(countryMap[country])

queries = int(input())
for i in range(queries):
    data = input().split()
    country = data[0]

    # Sorts the list if it has not been sorted before:
    if(not sortedMap.__contains__(country)):
        countryMap[country].sort()
        sortedMap[country] = country

    visit = int(data[1])

    l = countryMap[country]
    print(l[visit-1])