#include <stdio.h>

int main()
{   
    long long int N = 0;
    long long int M = 0;
    long long int Q = 0;
    
    scanf("%lld %lld", &N, &M);
    for(long long int i = 1; i <= N; i++){
        if(i > M)
            break;
        
        if(M%i == 0 && (long long int) M/i <= N){
            Q ++;
        }
    }
    
    printf("%lld", Q);
    return 0;
}
