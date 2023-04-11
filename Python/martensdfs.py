# Solution to the problem: https://open.kattis.com/problems/martensdfs

''' 
Hard Ranking Problem : Mårtens DFS
This problem is about verifying a DFS through a graph. The way I solved it is to use a stack (since stacks are the way we make DFS searches).
We can think of a valid DFS as a search that always exhaust its nodes on the stack. As such, if we get a node, perhaps one that would be visited
in a BFS rather than a DFS, we can compare the nodes on the stack. For every node pushed to the stack, if we are to pop them, the condition that
every such node on the stack needs to have visited all their nodes before popping. In this way we can discern between BFS and DFS, or any other
scheme for that matter. We force this condition on Mårtens tour. 
'''

def init_adj_list(E):
    adj_list = {}
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
    return adj_list

def is_valid_dfs(adj_list, path):
    # For a special case if there was a tour with no nodes at all, I wasne't sure so I wanted to run a case that would get run time error:
    if len(path) == 0:
        print("NO" + str(adj_list["HELLo"]))
        return []
    else:
        # 1. Else we initiate a stack and a visited Hashmap:
        stack = [path[0]]
        visited = {path[0]: True}

        # 2. We iterate over every node in the tour as vertex:
        for i in range(1, len(path)):
            vertex = path[i]
            
            # 3. For as long as the stack has nodes in it we do two operations:
            while len(stack) > 0:
                top = stack[len(stack) - 1]

                # 4. Operation 1: If the node on top of the stack is a parent to the new node we append the new node (Valid DFS)
                if vertex in adj_list[top]:
                    stack.append(vertex)
                    visited[vertex] = True
                    break
                
                # 5. Operation 2: If the node on top of the stack is not a parent we pop the stack provided that the exhaustion condition holds:
                else:
                    for next_vertex in adj_list[stack[len(stack) - 1]]:
                        if next_vertex not in visited:
                            return []
                    stack.pop()
        return stack

if __name__ == "__main__":

    # 1. Initiate the data for visiting a graph:
    V,E = list(map(int,input().split()))
    adj_list = init_adj_list(E)
    path = list(map(int,input().split()))
    visited = {}

    # 2. Push the data into the is_valid_graph:
    stack = is_valid_dfs(adj_list,path)

    # 3. If the length of nodes does not match or if the valid_dfs was a failure we print no, else we print yes:
    if(len(stack) == 0 or not len(path) == V):
        print("NO")
    else:
        print("YES")
