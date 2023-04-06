// A solution to the problem: https://open.kattis.com/problems/countdoubles


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
    // 1. Input:
    int n;
    int m;    
    cin >> n;
    cin >> m;
    int arr[n];

    // 2. Fill the int array:
    for(int i = 0; i < n; i++){
        int a;
        cin >> a;
        arr[i] = a;
    }
    
    // 3. Take out every substring of size m and see how many even elements there are:
    int total_even = 0;
    for(int i = m-1; i < n; i++){
        int even = 0;
        for(int j = i - (m-1); j < i+1; j++){
            //cout << arr[j] << " ";
            if(arr[j]%2 == 0){
                even ++;
                if(even == 2){
                    total_even ++;
                    break;
                }
            }
        }
    }
    
    // 4. Print the answer:
    cout << total_even;
    return 0;
}
