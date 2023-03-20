// A solution to the problem: https://open.kattis.com/problems/battlesimulation

import java.util.Scanner;
public class mech {
    public static void main(String[]args){
        // 1. Read in the input and define a stringbuilder for faster string concatenation, used in response to the input:
        Scanner sc = new Scanner(System.in);
        String monsterLine = sc.nextLine();
        StringBuilder response = new StringBuilder();
        
        // 2. Since the problem size is large we linearly look at every character and if we can the two sucessors: 
        for (int i = 0; i < monsterLine.length(); i++){
            char first = monsterLine.charAt(i);
            boolean comboBreaker = false;
            
            // 3. We define some bounds and we check the second and third character for this combo attack specified:
            if(i < monsterLine.length()-2){
                char second = monsterLine.charAt(i+1);
                char third = monsterLine.charAt(i+2);
                
                // 4. If we can find the combo attack we set the flag and increment i with 2 to skip those for the next iteration:
                if (first != second && first != third && second != third){
                    response.append("C");
                    comboBreaker = true;
                    i += 2;
                }
            }
            
            // 5. Lastly we append the counter, provided that the combo attack was not used:
            if(!comboBreaker){
                if(first == 'R'){
                    response.append("S");
                }
                else if(first == 'B'){
                    response.append('K');
                }
                else{
                    response.append('H');
                }
            }

        }
        
        // 6. String concatenation is very slow in Java so for our answer we use a stringbuilder (lest we get "time limit exceeded"):
        System.out.println(response.toString());
    }
}
