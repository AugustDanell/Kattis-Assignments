// A solution to the problem: https://open.kattis.com/problems/bungeebuilder


#include <vector>
#include <iostream>
using namespace std;

int max(int x1, int x2){
    if(x1 > x2){
        return x1;
    }
    return x2;
}

int main()
{   
    // Input and initialization:
    int n;
    cin >> n;
    int heights[n];
    for(int i = 0; i < n; i++){
        int a;
        cin >> a;
        heights[i] = a;
    }
    
    int start = heights[0];
    int local_highest = 0;
    int local_min = -1;
    int global_height = 0;
    
    // Loop over every mountain:
    for(int i = 1; i < n; i++){
        int current = heights[i];
        
        // 1. Initiate a new starting point for coming iterations and calculate a best height so far:
        if (current > start){
            if (local_min != -1){
                int height = start - local_min;
                if(height > global_height){
                    global_height = height;
                }
            }
            start = current;
            local_highest = 0;
            local_min = -1;
        }
        
        // 2. If we find a new peak less than current start, let it be a endpoint for now:
        else if(current > local_highest){
            local_highest = current;
            if(local_min != -1){
                int height = current - local_min;
                if(height > global_height){
                    global_height = height;
                }
            }
        }
        
        // 3. If we find a new local min update accordingly:
        if(local_min == -1 || current < local_min){
            local_min = current;
        }
        
        // 4. Sometimes the current endpoint should be the new start but it does not update:
        else{
            int height = current - local_min;
            if (height > global_height){
                global_height = height;
            }
        }
    }

    cout << global_height;
    
    return 0;
}
