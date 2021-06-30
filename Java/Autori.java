import java.util.Scanner;

/**
 * Created by August DH on 2017-05-15.
 */
public class Autori {
    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);

        String input = sc.nextLine();
        String returnString = "";

        returnString += input.charAt(0);

        for(int i = 1; i < input.length(); i++){
            if(input.charAt(i) == '-' && i != input.length()-1){
                returnString += input.charAt(i+1);
            }
        }

        System.out.print(returnString);
    }
}
