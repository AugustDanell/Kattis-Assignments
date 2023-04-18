# A solution to the problem: https://open.kattis.com/problems/speedrun

'''
    General Solution:
    Taking some inspiration from: https://www.geeksforgeeks.org/scheduling-in-greedy-algorithms/
    "It turns out that this algorithm always produces an optimal solution..."
    So we go by the greedy strategy to always choose the task finishing the earliest:
'''

if __name__ == "__main__":
    G,N = list(map(int,input().split()))
    task_list = []
    for _ in range(N):
        task_list.append(list(map(int,input().split())))
    task_list = sorted(task_list, key=lambda x: x[1])

    time = 0
    completed_tasks = 0
    for task in task_list:
        if time <= task[0]:
            time = task[1]
            completed_tasks += 1

    #print(completed_tasks)
    print("YES" if completed_tasks == G else "NO")
