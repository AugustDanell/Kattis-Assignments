#include <stdio.h>

int main()
{
    long long a;
    scanf("%lld", &a);
    
    if(a % 2 == 1){
        printf("Alice");
    }
    else{
        printf("Bob");
    }
    return 0;
}
