import java.util.Scanner;

/**
 * Created by August DH on 2016-12-14.
 */
public class AlphabetSpam {
    public static void main(String[]args){
        Scanner sc = new Scanner (System.in);
        String input = sc.nextLine();

        double whitespace = 0;
        double symbol = 0;
        double UPPERCASE = 0;
        double UNDERCASE = 0;
        int total = input.length();

        for(int i = 0; i < input.length(); i++){
            if((int)input.charAt(i) == 95){
                whitespace++;
            }
            if((int)input.charAt(i) >= 65 && (int)input.charAt(i) <= 90){
                UPPERCASE ++;
            }
            if((int)input.charAt(i) >=97 && (int)input.charAt(i) <= 122){
                UNDERCASE ++;
            }
            if(((int)input.charAt(i) >= 33 && (int)input.charAt(i) <= 64) || ((int)input.charAt(i) >= 91 && (int)input.charAt(i)<= 94 ) || ((int)input.charAt(i) >= 123 && (int)input.charAt(i) <= 126) || ((int)input.charAt(i) == 96)){
                symbol ++;
            }
        }
        double sumOfWhitespace = whitespace/total;
        double sumOfUPPERCASE = UPPERCASE/total;
        double sumOfUNDERCASE = UNDERCASE/total;
        double sumOfSymbol = symbol/total;

        System.out.println(sumOfWhitespace);
        System.out.println(sumOfUNDERCASE);
        System.out.println(sumOfUPPERCASE);
        System.out.print(sumOfSymbol);

    }
}
