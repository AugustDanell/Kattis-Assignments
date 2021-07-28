#include <stdio.h>

int main()
{   
    int stops;
    scanf("%d", &stops);
    int start_time = 0;
    int stopped_time = 0;
    int total_time = 0;
    int time;
    
    for(int i = 0; i < stops; i++){
        scanf("%d", &time);
        
        if(i%2 == 0){
            start_time = time;
            stopped_time = 0;
        }
        else{
            stopped_time = 1;
            total_time += time - start_time;
        }
        
    }
    
    if(stopped_time == 0){
        printf("still running");
    }
    else{
        printf("%d", total_time);
    }
        
    
    
    return 0;
}
