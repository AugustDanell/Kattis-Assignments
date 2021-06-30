import java.util.Scanner;

/**
 * Created by August DH on 2017-02-03.
 */
public class MixedFractions2 {
    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);
        boolean run = true;
        StringBuilder builder = new StringBuilder();

        while(run){
            String input = sc.nextLine();
            if(!input.equals("0 0")){
                String[] splittedInput = input.split(" ");
                int numerator = Integer.parseInt(splittedInput[0]);
                int denominator = Integer.parseInt(splittedInput[1]);
                int whole = 0;

                while(numerator >= denominator){
                    numerator = numerator - denominator;
                    whole++;
                }
                builder.append(whole +" " + numerator+" / " + denominator + "\n");

            }
            else{
                run = false;
            }

        }

        System.out.println(builder.toString());
    }
}
