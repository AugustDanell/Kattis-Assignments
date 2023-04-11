# A solution to the problem: https://open.kattis.com/problems/dominos

'''
General Solution:
At first glance this problem is easily solved using a directed graph. We can keep track of what dominos are never visited and save them as dominos
used to start the chain reaction. However, once we have done that we stand before a problem: In some cases we may not visit every node in a graph,
depending on where we start. To solve that we can transform the directed graph to an undirected graph. 
'''

def dfs(start_node, adj_list, visited):
    to_visit = [start_node]
    visited[start_node] = True

    while(len(to_visit) > 0):
        current = to_visit.pop()

        if not current in adj_list:
            continue

        for next_node in adj_list[current].keys():
            if next_node in visited:
                continue
            else:
                to_visit.append(next_node)
                visited[next_node] = True

if __name__ == "__main__":
    testcases = int(input())
    for _ in range(testcases):
        V,E = list(map(int,input().split()))
        adj_list = {}
        start_nodes = {}

        # 1. Create an undirected graph and save the nodes that have are never visited (so called starting nodes).
        for _ in range(E):
            v1,v2 = list(map(int,input().split()))
            if v1 in adj_list:
                adj_list[v1][v2] = True
            else:
                adj_list[v1] = {v2:True}
            if v2 in adj_list:
                adj_list[v2][v1] = True
            else:
                adj_list[v2] = {v1:True}

            if not v1 in start_nodes:
                start_nodes[v1] = True
            start_nodes[v2] = False


        # 2. Initiate a list over visited nodes and a counter for how many nodes have been visited (knocked over):
        visited = {}
        push_over = 0
        
        # 3. Start with the nodes that are never visited. They have to be visited once so let them knock over as many dominos as they can:
        for trigger_node in start_nodes.keys():
            if start_nodes[trigger_node] == False:
                continue
            dfs(trigger_node, adj_list, visited)
            push_over += 1
        
        # 4. If we still have unvisited nodes we visit them in the DIRECTED graph. We have made it directed so that we automatically connect the graph, i.e, find the best:
        for node in range(1, V+1):
            if node in visited:
                continue
            else:
                dfs(node, adj_list, visited)
                push_over +=1
        
        # 5. Lastly just print out the result:
        print(push_over)
