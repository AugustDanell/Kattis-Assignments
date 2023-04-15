// A solution to the problem: https://open.kattis.com/problems/positivedivisors

#include <iostream>
#include <vector>
#include <math.h>
#include <unordered_map>
using namespace std;

int main(){
    unsigned long long n;
    cin >> n;
    vector<unsigned long long> factors;
    unordered_map<int, bool> umap;
    
    for(unsigned long long i = 1; i <= floor(sqrt((n))); i++){
        if(n%i == 0){
            cout << i << endl;
            unsigned long long key = i;
            if (umap.find(key) == umap.end()&& key != n/i){
                factors.push_back(n/i);
                umap[key] = true;
            }
        }
    }
    for(int i = 0; i < factors.size(); i++){
        cout << factors[factors.size() -1 - i] << endl;
    }
    
    return 0;
}
