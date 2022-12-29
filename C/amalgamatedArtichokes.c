#include <stdio.h>
#include <math.h>

float price(int p, int a, int b, int c, int d, int k){
    return (float)(p*(sin(a*k + b) + cos(c*k + d) + 2));
}

int main()
{   
    int p; int a; int b; int c; int d; int n;
    scanf("%d %d %d %d %d %d", &p, &a, &b, &c, &d, &n);
    float largestDecline = 0.0f;
    float stocks[n-1]; // Not needed
    float highestStock = 0.0f;
    
    // Read in stocks and compare to our global high:
    for(int i = 0; i < n; i++){
        float stock = price(p, a, b, c, d, i+1);
        
        if(highestStock < stock){
            highestStock = stock;
        }
        
        float decline = stock - highestStock;
        
        if(decline < largestDecline){
            largestDecline = decline;
        }
    }
    
    if(largestDecline < 0)
        printf("%f", -largestDecline);
    else
        printf("0.00");
    
    return 0;
}
