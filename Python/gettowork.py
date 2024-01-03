def minimizeDrivers(town, employeeMap):
    if town not in employeeMap:
        return 0

    employees = employeeMap[town]
    sortedEmployees = list(sorted(employees, key= lambda x: x[1], reverse=True))
    acc = 0
    for i in range(len(sortedEmployees)):
        employee = sortedEmployees[i]
        acc += employee[1]
        if acc >= len(sortedEmployees):
            return i+1
    return -1

if __name__ == "__main__":
    cases = int(input())
    for c in range(cases):
        towns, office = list(map(int, input().split()))
        employees = int(input())
        employeeMap = {}
        for _ in range(employees):
            employee = list(map(int,input().split()))
            if employee[0] != office:
                if employee[0] in employeeMap:
                    employeeMap[employee[0]].append(employee)
                else:
                    employeeMap[employee[0]] = [employee]

        possible = True
        ans = []

        # Inclusive Iteration:
        for town in range(1, towns+1):
            drivers = minimizeDrivers(town, employeeMap)
            if drivers == -1:
                possible = False
                break
            else:
                ans.append(drivers)

        ans = list(map(str, ans))
        if possible:
            print("Case #{0}: {1}".format(c+1, " ".join(ans)))
        else:
            print("Case #{0}: IMPOSSIBLE".format(c+1))