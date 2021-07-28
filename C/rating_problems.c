#include <stdio.h>

int main()
{
    int judges;
    int scored;
    scanf("%d%d", &judges, &scored);
    float left = judges - scored;

    int score = 0;
    int judge = 0;
    for(int i = 0; i < scored; i++){
        scanf("%d", &judge);
        score += judge;
    }
    

    float top_score = (score+left*3)/judges;
    float bot_score = (score-left*3)/judges;
    
    printf("%f %f", bot_score, top_score);
}
