// Solution to the problem: 

// Alternative solution in C:
/*
#include<stdio.h>
int main(){long n;scanf("%ld",&n);printf("%ld", (long)n/2);return 0;}
*/

#include <iostream>
#include <cmath>
using namespace std;



int main(){
    long n;
    cin >> n;
    if (n == 2 || n == 3){
        cout << 1;
    }
    else {
        cout << (long)(n/2);
    } 
    return 0;
}
