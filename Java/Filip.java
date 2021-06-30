import java.util.Scanner;

/**
 * Created by August DH on 2017-04-22.
 */
public class Filip {
    public static int reverse(String input){
        String returnString = "";

        for(int i = input.length()-1; i >= 0; i--){
            returnString += input.charAt(i);
        }

        return Integer.parseInt(returnString);
    }

    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);
        String input = sc.nextLine();
        String[] splitted = input.split(" ");

        // Funkar - System.out.println(splitted[0] + splitted[1]);

        int x = reverse(splitted[0]);
        int y = reverse(splitted[1]);

        if(x > y){
            System.out.println(x);
        }else{
            System.out.println(y);
        }
    }
}
