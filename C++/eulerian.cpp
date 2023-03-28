// Solution to the problem: https://open.kattis.com/problems/eulerian

#include <iostream>
using namespace std;

int main()
{   
    int V, E;
    scanf("%d %d", &V, &E);
    int in[V];
    int out[V];
    for(int i = 0; i < V; i++){
        in[i] = 0;
        out[i] = 0;
    }
    
    
    for(int i = 0; i < E; i++){
        int v1,v2;
        scanf("%d %d", &v1, &v2);
        in[v1-1] +=1;
        out[v2-1] += 1;
    }
    
    int start = -1;
    int end = -1;
    int impossible = 0;
    
    for(int i = 0; i < V; i++){
        if(in[i] == out[i]){
            continue;
        }
        else if((in[i] + 1) == out[i]){
            if (end != -1){
                impossible = 1;
                break;
            }
            else{
                end = (i+1);
            }
        }
        else if((out[i]+1) == in[i]){
            if(start != -1){
                impossible = 1;
                break;
            }
            else{
                start = (i+1);
            }
        }
        else{
            impossible = 1;
            break;
        }
    }
    
    if(impossible == 1){
        cout << "no";
    }
    else if(start == -1 && end == -1){
        cout << "anywhere";
    }
    else{
        cout << start << " " << end;
    }
    
    return 0;
}
