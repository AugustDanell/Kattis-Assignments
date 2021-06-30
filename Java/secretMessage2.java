import java.util.Scanner;

/**
 * Created by August DH on 2017-02-17.
 */
public class secretMessage2 {
    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);
        int cases = sc.nextInt();
        sc.nextLine();

        StringBuilder builder = new StringBuilder();
        for(int i = 0; i < cases; i++){
            String input = sc.nextLine();
            int originalSizeInput = input.length();
            int smallestSquare = 0;
            int counter = 1;

            while(smallestSquare <originalSizeInput){
                smallestSquare = counter * counter;
                counter ++;
            }
            //Now we have our smallestSquare
            //Counter should be one more than the sqrroot of smallestSquare

            counter --;

            for(int j = 0; j < (smallestSquare - originalSizeInput); j++){
                input += "*";
            }

            //System.out.println(input);
            //System.out.print(counter);
            for(int j = 0; j < counter; j++){
                for(int k = 1; k < counter+1; k++) {
                    if (input.charAt(input.length()-(k*counter)+j) != '*') {
                        builder.append("" + input.charAt(input.length()-(k*counter)+j));
                   }
                }
            }

            builder.append("\n");
        }

        System.out.print(builder.toString());
    }
}
