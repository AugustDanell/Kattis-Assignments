#include <stdio.h>

void oddities(int n){
  int c;
  for(int i = 0; i < n; i++){
    scanf("%d", &c);
    if(c%2 == 0){
      printf("%d is even\n", c);
    }
    else{
      printf("%d is odd\n", c);
    }
  }
}

int main(){
  int n;
  scanf("%d", &n);

  oddities(n);
  return 0;
}