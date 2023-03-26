// Kattis Solution to: https://open.kattis.com/problems/countingdays

//#include "countingdays.h"
#include <iostream>

// 1. Initiate some global constants:
int h = 0;
int m = 0;
int d = 1;
using namespace std;

// 2. Define the look at clock such that we increment the day counter if we recieve a time that is less than our last logged one:
void lookAtClock(int hours, int minutes) {
    if (hours < h || (hours == h && minutes < m)){
        d ++;
    }
    h = hours;
    m = minutes;
}

int getDay() {
    return d;
}


