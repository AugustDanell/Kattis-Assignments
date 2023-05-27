// My 691th Solution. Basically a BFS between node 1 and N. Solution to the problem: https://open.kattis.com/problems/onaveragetheyrepurple

/* General Solution: BFS
   We initialize an adjacency list and then we pass that into a BFS function.
   We then find the shortest route from node 1 to node N. The answer is then
   the length of the shortest route - 1. 
*/

#include <iostream>
#include <unordered_map>
#include <vector>
using namespace std;

int BFS(int start, int end, unordered_map<int, unordered_map<int, bool>> umap){
    vector<int> to_visit;
    to_visit.push_back(start);
    to_visit.push_back(0);
    unordered_map<int, bool> visited;
    visited[start] = true;
    int index = 0;
    
    while (to_visit.size() > index){
        int current_node = to_visit[index];
        int current_depth = to_visit[index+1];
        //cout << "current node: " << current_node << endl;
        index += 2;
        
        if(current_node == end){
            return current_depth;
        }
        if(umap.find(current_node) == umap.end()){
            continue;
        }
        else{
            for(auto kv : umap[current_node]) {
                //cout << "test: " << kv.first << endl;
                if (visited.find(kv.first) == visited.end()){
                    //cout << "append" << endl;
                    visited[kv.first] = true;
                    to_visit.push_back(kv.first); 
                    to_visit.push_back(current_depth+1);
                }
            } 
        }
        
    }
    
    
    return -1;
}

int main()
{
    int N;
    cin >> N;
    int M;
    cin >> M;
    
    // Initialize a adjacency list:
    unordered_map<int, unordered_map<int,bool>> umap;
    for(int i = 0; i < M; i++){
        int a;
        int b;
        cin >> a;
        cin >> b;
        
        if (umap.find(a) == umap.end()){
            unordered_map<int, bool> inner_map;
            inner_map[b] = true;
            umap[a] = inner_map;
        }
        else{
            umap[a][b] = true;
        }
        
        if (umap.find(b) == umap.end()){
            unordered_map<int, bool> inner_map;
            inner_map[a] = true;
            umap[b] = inner_map;
        }
        else{
            umap[b][a] = true;
        }
    }
    
    cout << BFS(1, N, umap) - 1 << endl;
    return 0;
}
