// A solution to the problem: https://open.kattis.com/problems/lastfactorialdigit

#include <stdio.h>
int tail_factorial(n,tail){
    if(n == 1 || n == 0){
        return tail;
    }
    else{
        tail *= n;
        return tail_factorial(n-1, tail);
    }
}


int main()
{
    int testcases = 0;
    scanf("%d",&testcases);
    
    for(int i = 0; i < testcases; i++){
        int fac = 0;
        scanf("%d", &fac);
        int factorial = tail_factorial(fac, 1);
        int mod = factorial % 10;
        printf("%d\n",mod);
    }

    return 0;
}
