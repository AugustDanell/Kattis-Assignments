import java.util.Scanner;

/**
 * Created by August DH on 2016-12-11.
 */
public class Aaaah {
    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);

        //Inputs for the program
        String inputedString = sc.nextLine();
        String aaah = sc.nextLine();

        if(inputedString.charAt(inputedString.length()-1) == 'h' && aaah.charAt(aaah.length()-1) == 'h') {
            if (inputedString.length() >= aaah.length()) {
                System.out.print("go");
            } else {
                System.out.print("no");
            }
        }
    }
}
