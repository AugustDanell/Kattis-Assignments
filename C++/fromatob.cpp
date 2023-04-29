// Solution to the problem: https://open.kattis.com/problems/fromatob

#include <iostream>
using namespace std;

int main()
{
    int a;
    int b;
    cin >> a;
    cin >> b;
    int operations = 0;
    
    while (a > b){
       if (a % 2 == 0){
           operations += 1;
           a /= 2;    
       }
       else{
           a ++;
           operations += 2;
           a /= 2;
       }
    }
    
    cout << (b-a) + operations;

    return 0;
}
