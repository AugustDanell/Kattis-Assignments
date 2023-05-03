// A solution to the problem: https://open.kattis.com/problems/titlecost
// The iomanip library allows for us to define specific precisions. 

#include <iostream>
#include <string>
#include <iomanip>
using namespace std;

void print_min(string str, double num){
    if ((double)str.size() < num){
        cout << str.size();
    }
    else{
        cout << setprecision(15) << num; 
    }
}

int main()
{
    string str;
    double num;
    cin >> str >> num;
    print_min(str, num);
    return 0;
}
