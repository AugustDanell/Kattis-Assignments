#include <stdio.h>

int abs2(int a, int b){
    if(a > b)
        return a - b;
    return b - a;
}

int main()
{
    int a; int b; int c;
    scanf("%d %d %d", &a, &b, &c);
    
    if(b*2 == a + c)
        printf("cruised");
    else if((b > a && b > c) || (b < a && b < c))
        printf("turned");
    else if(((b > a && b < c) || (b < a && b > c)) && abs2(a,b) < abs2(b,c))
        printf("accelerated");
    else
        printf("braked");

    
    
    return 0;
}
