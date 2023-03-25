// A solution to the problem: https://open.kattis.com/problems/evenup

#include <iostream>
#include <string>
#include <vector>
using namespace std;

// max is a function that simply returns the greater value of 2 arguments:
int max(int x1, int x2){
    if (x1 >= x2){
        return x1;
    }
    return x2;
}

int main()
{   
    // 1. Input:
    int n;
    cin >> n;
    vector<int> cards;

    // 2. Pump in numbers to the vector 'cards'
    for(int i = 0; i < n; i++)
    {
        int number;
        cin >> number;
        cards.push_back(number);
    }
    
    // 3. Iterate over index in the range of (0, N-2), inclusively:
    for (int index = 0; index < cards.size() - 1;) {
        
        // 4. Initiate 2 elements. Current, which is the card on this index and next which is the element on index + 1: 
        int current = cards[index];
        int next = cards[index+1];
        
        // 5. If current and next make for an even sum we remove them and we safely decrement index. Else we increment it:
        if ((current + next)%2 == 0) {
            cards.erase(cards.begin() + index, cards.begin() + index + 2);
            index = max(index - 1, 0);
        } 
        else {
        
            index++;
        }
        
        // 6. Throw in a safety check for run time errors:
        if(cards.empty()){
            break;
        }
    }
    
    // 7. Print the remaining size of the vector:
    cout << cards.size();
    return 0;
}
