//
// Created by August DH on 2017-06-18.
//
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main() {
    int searchedForInt;
    char returnString[64] = "Hello";
    int found = 0;  //Improvised boolean as this is my first time in C and I can't get anything to work it would seem and I am slightly annoyed because of it. But I do like this language.
    scanf("%d", &searchedForInt);
        for (int i = 0; i <= 150000; i++) {
            for (int j = i; j <= 150000; j++) {
                if (j * j - i * i == searchedForInt) {
                    char a[10];
                    char b[10];

                    sprintf(a, "%d", i);
                    sprintf(b, "%d", j);

                    //itoa(i, a, 10);
                    //itoa(j, b, 10);

                    strcpy(returnString, a);
                    strcat(returnString, " ");
                    strcat(returnString, b);
                    found = 1;

                    break;
                }

                if(((j * j) - (i * i)) > 200000){
                    break;
                }
            }


            if (found == 1) {
                break;
            }
        }

    if(found == 0){
        strcpy(returnString, "impossible");
    }

    printf("%s", returnString);
    return 0;
}
