# problem: https://open.kattis.com/problems/planets2

if __name__ == "__main__":
    
    # 1. Read in data:
    P = int(input())
    specyToPlanet = {}
    planetToNumber = {}
    
    # 2. Iterate over each planet:
    for _ in range(P):
        
        # 3. Read in data and init maps:
        data = input().split()
        name = data[0]
        n = int(data[1])
        species = data[2:]
        planetToNumber[name] = 0
        for specy in species:
            specyToPlanet[specy] = name
    
    # 4. Make queries for each alien visiting the starport:
    queries = int(input())
    for _ in range(queries):
        
        # 5. For each specy, check the reverse mapping to get the planet and increment it:
        size, specy = input().split()
        size = int(size)
        fromPlanet = specyToPlanet[specy]
        planetToNumber[fromPlanet] += size
    
    # 6. Sort the planets in lexiographical order:
    lexSortedPlanets = sorted(planetToNumber.keys())
    for planet in lexSortedPlanets:
        
        # 7. Print the planet and how many ppl came from that planet:
        print(planet, planetToNumber[planet])
