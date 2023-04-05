// Solution to the problem: https://open.kattis.com/problems/undeadoralive

#include <iostream>
using namespace std;

int main()
{   
    string str;
    getline(cin, str);
    bool human = false;
    bool zombie = false;
    
    for(int i = 1; i < str.size(); i++){
        char current_chr = str.at(i);
        char prev_chr = str.at(i-1);
        
        if(prev_chr == ':' && current_chr == ')'){
            human = true;
        }
        else if(prev_chr == ':' && current_chr == '('){
            zombie = true;
        }
        
    }
    
    if (human && zombie){
        cout << "double agent";
    }
    else if(human){
        cout << "alive";
    }
    else if(zombie){
        cout << "undead";
    }
    else{
        cout << "machine";
    }
    return 0;
}
