import java.util.Scanner;

/**
 * Created by August DH on 2016-12-13.
 */
public class Cryptograph {
    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);
        String input = sc.nextLine();
        int letterToSubstitute = 0;
        int days = 0;

        for(int i = 0; i < input.length(); i++){
            letterToSubstitute = letterToSubstitute % 3;
            if(letterToSubstitute == 0 && input.charAt(i) != 'P'){
                days ++;
            }

            if(letterToSubstitute == 1 && input.charAt(i) != 'E'){
                days ++;
            }

            if(letterToSubstitute == 2 && input.charAt(i) != 'R'){
                days ++;
            }

            letterToSubstitute ++;
        }

        System.out.print(days);
    }
}
