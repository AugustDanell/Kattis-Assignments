//#include "vectorfunctions.h"
#include <vector>
#include <iostream>
using namespace std;

void backwards(std::vector<int>& vec){
    for(int i = 0; i < (int)vec.size()/2; i++){
        int temp = vec[i];
        vec[i] = vec[(vec.size()-1)-i];
        vec[(vec.size()-1)-i] = temp;
    }
}

std::vector<int> everyOther(const std::vector<int>& vec){
    std::vector<int> v;
    for(int i = 0; i < vec.size(); i+= 2){
        v.push_back(vec[i]);
    }
    return v;
}

int smallest(const std::vector<int>& vec){
    int smallest = 0;
    for(int i = 0; i < vec.size(); i++){
        if(i == 0){
            smallest = vec[i];
        }
        else if(vec[i] < smallest){
            smallest = vec[i];
        }
        
    }
    return smallest;
}

int sum(const std::vector<int>& vec){
    int s = 0;
    for(int i = 0; i < vec.size(); i++){
        s += vec[i];
    }
    return s;
}


int veryOdd(const std::vector<int>& suchVector){
    int oddIntegers = 0;
    for(int i = 1; i < suchVector.size(); i+=2){
        if(suchVector[i]%2 == 1){
            oddIntegers ++;
        }
    }
    
    return oddIntegers;
}
