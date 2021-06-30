import java.util.Scanner;

/**
 * Created by August DH on 2017-04-04.
 */
public class hiddenPassword2 {
    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);
        String input = sc.nextLine();
        String[] splitted = input.split(" ");

        boolean failed = false;
        String password = splitted[0];
        String message = splitted[1];

        boolean[] passes = new boolean[password.length()];
        for(int i = 0; i < password.length(); i++){
            passes[i] = false;
        }

        char searchedforLetter = password.charAt(0); //Startvalue
        String UnpermittedLetters = password.substring(1,password.length());

        int iteration = 0;
        for(int i = 0; i < message.length(); i++){
            //System.out.print(message.charAt(i));
            if(message.charAt(i) == searchedforLetter && !passes[password.length()-1]){
                passes[iteration] = true;
                iteration ++;
                if(!passes[password.length()-1]) {
                    searchedforLetter = password.charAt(iteration);
                    UnpermittedLetters = password.substring(1 + iteration, password.length());
                }
            }
            else if(UnpermittedLetters.contains(("" + message.charAt(i))) && !passes[password.length()-1]){
                failed = true;
                break;
            }
        }

        if(!passes[password.length()-1]){
            failed = true;
        }

        if(!failed){
            System.out.println("PASS");
        }
        else{
            System.out.println("FAIL");
        }
    }
}
