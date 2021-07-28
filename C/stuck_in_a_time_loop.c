#include <stdio.h>

int main()
{
    long a;
    scanf("%ld", &a);
    long i = 0;
    while(i < a){
        printf("%d Abracadabra\n", (i)+1);
        i ++;
    }   
}
