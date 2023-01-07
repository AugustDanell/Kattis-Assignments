#include <stdio.h>

int main()
{
    int n;
    char s[100000];
    scanf("%d %s", &n, &s);
    
    int coffees = 0;
    int lectures = 0;
    for(int i = 0; i < n; i++){
        if(s[i] == '1'){
            coffees = 2;
            lectures ++;
        }
        else{
            if(coffees > 0){
                coffees --;
                lectures ++;
            }
        }
    }
    
    printf("%d", lectures);
    return 0;
}
