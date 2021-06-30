import java.util.Arrays;
import java.util.Scanner;

/**
 * Created by August DH on 2017-01-01.
 */
public class Simplicity {
    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);
        String input = sc.nextLine();
        int sameLetters[] = new int[input.length()];
        for(int i = 0; i < input.length(); i++){
            //sameLetters[i] = 1;
            for(int j = 0; j < input.length(); j++){
                if(j!=i && input.charAt(j)==input.charAt(i)){
                    sameLetters[j]++;
                }
            }
        }

        for(int i = 1; i < input.length(); i++){
            int x = sameLetters[i];
            int j = i - 1;
            while(j >= 0 && sameLetters[j] > x){
                sameLetters[j+1] = sameLetters[j];
                j = j - 1;
            }
            sameLetters[j+1] = x;
        }

        String sameToString = Arrays.toString(sameLetters);
        boolean lastIndexEqualsFirstIndex = false;
        int lastIndex = sameLetters[input.length()-1] + 1;
        if((input.length()-lastIndex) == 0){
            lastIndexEqualsFirstIndex = true;
            System.out.println("0");
        }
        else {
            int secondLastIndex = sameLetters[input.length() - 1 - lastIndex] + 1;
            String simplicityString = input.substring(0, (input.length()) - lastIndex - secondLastIndex);

            //System.out.println(Arrays.toString(sameLetters));
            System.out.println(simplicityString.length());
        }
    }
}
