// 663th Kattis. A solution to the problem: https://open.kattis.com/problems/primereduction

/* General Solution idea:
*  1. Use a square-root-Sieves as factorization scheme.
*  2. Use a sum() function to sum the square-root.
*  3. Iteratively continue until we find a prime, then print it and its iterations
*/


#include <iostream>
#include <vector>
#include <cmath>
#include <unordered_map>
using namespace std;

// Function to calculate a sum of a vector:
int sum(vector<int> factors){
    int s = 0;
    for(int i = 0; i < factors.size(); i++){
        s += factors[i];
    }
    return s;
}

// Function to factorize N into a vector of factors: 
vector<int> factorize(int N){
    vector<int> factors;
    int end = (int)sqrt(N);
    for(int i = 2; i <= end; i++){
        while(N%i == 0){
            factors.push_back(i);
            N = (int)N/i;
        }
    }
    
    if(N != 1){
        factors.push_back(N);
    }
    return factors;
}

int main()
{   
    unordered_map<int, int> umap;
    while (true){
        int n;
        cin >> n;
        if (n == 4){
            break;
        }
        else{
            int iterations = 1;
            while (true){
                 if (umap.find(n) != umap.end()){
                     cout << n << " " << (iterations - 1) + umap[n] << endl;;
                     break;
                 }
                 else{
                     vector<int> factors = factorize(n);
                     int s = sum(factors);
                     if(factors.size() == 1){
                         cout << factors[0] << " " << iterations << endl;
                         //umap[n] = iterations;
                         break;
                     }
                     else{
                         n = s;
                         iterations++;
                     }
                 }
            }
        }
    }
    
    return 0;
}
