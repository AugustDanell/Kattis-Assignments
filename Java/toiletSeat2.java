import java.util.Scanner;

/**
 * Created by August DH on 2017-03-09.
 */
public class toiletSeat2 {
    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);
        StringBuilder builder = new StringBuilder();

        String input = sc.nextLine();
        char startPosition = input.charAt(0);

        //First policy
        char currentPosition = startPosition;
        int adjustments = 0;
        for(int i = 1; i < input.length(); i++){
            if(currentPosition == 'U' && input.charAt(i) == 'D'){
                adjustments += 2;
                //If cp == U and charAt(i) == U - Do nothing.
            }
            else if(currentPosition == 'D' && input.charAt(i) == 'U'){
                adjustments ++;
            }
            else if(currentPosition == 'D' && input.charAt(i) == 'D'){
                adjustments ++;
            }

            currentPosition = 'U';
        }
        builder.append(adjustments + "\n");

        //Second policy
        currentPosition = startPosition;
        adjustments = 0;
        for(int i = 1; i < input.length(); i++){
            if(currentPosition == 'U' && input.charAt(i) == 'D'){
                adjustments ++;
                //If cp == U and charAt(i) == U - Do nothing.
            }
            else if(currentPosition == 'D' && input.charAt(i) == 'U'){
                adjustments += 2;
            }
            else if(currentPosition == 'U' && input.charAt(i) == 'U'){
                adjustments ++;
            }

            currentPosition = 'D';
        }
        builder.append(adjustments + "\n");

        //Third policy
        currentPosition = startPosition;
        adjustments = 0;
        for(int i = 1; i < input.length(); i++){
            if(currentPosition == 'U' && input.charAt(i) == 'D'){
                adjustments ++;
                //If cp == U and charAt(i) == U - Do nothing.
            }
            else if(currentPosition == 'D' && input.charAt(i) == 'U'){
                adjustments ++;
            }
            else if(currentPosition == 'U' && input.charAt(i) == 'U'){
                //adjustments ++;
            }

            currentPosition = input.charAt(i);
        }

        builder.append(adjustments + "\n");

        System.out.print(builder.toString());
    }
}
