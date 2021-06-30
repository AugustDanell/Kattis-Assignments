import java.util.Arrays;
import java.util.Scanner;

/**
 * Created by August DH on 2017-08-09.
 */
public class Veci5 {
    public static void main(String[]args) {
        Scanner sc = new Scanner(System.in);
        String number = sc.nextLine();
        int min = Integer.parseInt(number);
        int current = 100000000;    //Larger than it can be
        boolean permuted = false;

        //Sorting the string, to facilitate.
        char[] charizard = number.toCharArray();
        //Arrays.sort(charizard);

        number = new String(charizard);
        //number = new StringBuilder(number).reverse().toString();
        int greatestValue = 0;

        for(int k = 0; k < 1000; k++){
        for (int i = 0; i < number.length(); i++) {
            for (int j = 0; j < number.length(); j++) {
                char[] charArray = number.toCharArray();
                if (i != j) {
                    char temp = charArray[i];
                    charArray[i] = charArray[j];
                    charArray[j] = temp;

                    String permution = new String(charArray);
                    int value = Integer.parseInt(permution);
                    //System.out.println(value);
                    if (value > min && value < current) {
                       // System.out.println(value);
                        current = value;
                        permuted = true;
                        //number = "" + value;
                    }

                    if(value > greatestValue){
                        greatestValue = value;
                    }
                }
            }
        }
        if(permuted) {
            number = "" + current;
        }
        if(!permuted){
            number = "" + greatestValue;
            /* The reason as to why we save the greatest value is because
               it might be the case otherwise that we just iterate and iterate
               without ever getting past the min, despite being able to.
             */
        }
        //System.out.println(number);
        }

        if(!permuted){
            System.out.print("0");
        }
        else{
            System.out.print(current);
        }
    }
}
