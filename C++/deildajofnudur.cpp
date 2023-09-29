#include <iostream>
#include <map>
using namespace std;

bool validSubstring(int start, int end, string letters){
    map<char, int> frequencies;
    int index = start;
    while(index <= end){
        int key = letters.at(index);
        if(frequencies.count(key) == 0){
            frequencies[key] = 1;
        }
        else{
            frequencies[key] += 1;
        }
        index ++;
    }
    
    for(const auto &[keyOuter, valueOuter]: frequencies){
        for(const auto &[keyInner, valueInner]: frequencies)
        {
            if(valueOuter != valueInner){
                return false;
            }
        }
    }
    return true;
    
}

int getMax(int a, int b){
    if(a > b){
        return a;
    }
    return b;
}

int main() {
    int n;
    int globalMax = 0;
    string letters;
    cin >> n;
    cin >> letters;
    for(int i = 0; i < n; i++){
        for(int j = i; j < n; j++){
            if(validSubstring(i,j, letters)){
                globalMax = getMax(globalMax, 1+(j-i));
            }
        }
    }
    cout << globalMax; 
}  