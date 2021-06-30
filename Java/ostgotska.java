import java.util.Scanner;

/* First we may need a way of counting the words in the text. One such way
   could be to first trim the String of spaces and then for each time there is a space
   start a new word.

 */


public class ostgotska {

    public static double svenskaPercentage(String input){

        double got = 0;    // Östgötska counter
        double words = 1;  // Word counter - Forgot that the value should start of as one.
        boolean countedWord = false;

        for(int i = 0; i < input.length()-1; i++){
            if(input.charAt(i) == 'a' && input.charAt(i+1) == 'e' && !countedWord) {
                got++;
                countedWord = true;
            }

            if(input.charAt(i) == ' '){
                words ++;
                countedWord = false;
            }

        }

        return got/words;
    }
    public static void main(String[]args){
        Scanner sc = new Scanner (System.in);
        String input = sc.nextLine();

        input = input.trim(); // Removes excess spaces
        if(svenskaPercentage(input) >= 0.4){
            System.out.println("dae ae ju traeligt va");
        }
        else{
            System.out.println("haer talar vi rikssvenska");
        }

    }
}
