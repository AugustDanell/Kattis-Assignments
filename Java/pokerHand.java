import java.util.Scanner;

public class pokerHand {
    public static int checkMax (String inp){
        int max = 0;

        for(int i = 0; i < 13; i++){
            int count = 0;

            if( i == 0){
                for(int j = 0; j < 5; j++){
                    if(inp.charAt(j) == 'A'){
                        count ++;
                    }
                }
            }

            if( i == 1){
                for(int j = 0; j < 5; j++){
                    if(inp.charAt(j) == '2'){
                        count ++;
                    }
                }
            }

            if( i == 2){
                for(int j = 0; j < 5; j++){
                    if(inp.charAt(j) == '3')
                        count ++;
                }
            }

            if( i == 3){
                for(int j = 0; j < 5; j++){
                    if(inp.charAt(j) == '4')
                        count ++;
                }
            }

            if( i == 4){
                for(int j = 0; j < 5; j++){
                    if(inp.charAt(j) == '5')
                        count ++;
                }
            }

            if( i == 5){
                for(int j = 0; j < 5; j++){
                    if(inp.charAt(j) == '6')
                        count ++;
                }
            }

            if( i == 6){
                for(int j = 0; j < 5; j++){
                    if(inp.charAt(j) == '7')
                        count ++;
                }
            }

            if( i == 7){
                for(int j = 0; j < 5; j++){
                    if(inp.charAt(j) == '8')
                        count ++;
                }
            }

            if( i == 8){
                for(int j = 0; j < 5; j++){
                    if(inp.charAt(j) == '9')
                        count ++;
                }
            }

            if( i == 9){
                for(int j = 0; j < 5; j++){
                    if(inp.charAt(j) == 'T')
                        count ++;
                }
            }

            if( i == 10){
                for(int j = 0; j < 5; j++){
                    if(inp.charAt(j) == 'J')
                        count ++;
                }
            }

            if( i == 11){
                for(int j = 0; j < 5; j++){
                    if(inp.charAt(j) == 'Q')
                        count ++;
                }
            }

            if( i == 12){
                for(int j = 0; j < 5; j++){
                    if(inp.charAt(j) == 'K')
                        count ++;
                }
            }

            if(count > max){
                max = count;
            }
        }

        return max;
    }

    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);
        String input = sc.nextLine();
        String ranks = "" + input.charAt(0)
                          +  input.charAt(3)
                          +  input.charAt(6)
                          +  input.charAt(9)
                          +  input.charAt(12);

        System.out.println(checkMax(ranks));
    }
}
