import java.util.Scanner;

/**
 * Created by August DH on 2017-04-22.
 */
public class backspace {
    public static String reverse(String input){
        StringBuilder builder = new StringBuilder();
        for(int i = input.length()-1; i>= 0; i--){
            builder.append(input.charAt(i));
        }

        return builder.toString();
    }

    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);
        String input = sc.nextLine();

        StringBuilder builder = new StringBuilder();
        int ignoreCount = 0;
        for(int i = input.length()-1; i >= 0; i--){
            if(input.charAt(i) == '<'){
                ignoreCount ++;
            }
            else if(input.charAt(i) != '<' && ignoreCount > 0) {
                ignoreCount--;
            }
            else if(input.charAt(i) != '<' && ignoreCount == 0){
                builder.append(input.charAt(i));
            }
        }

        System.out.print(reverse(builder.toString()));
    }
}
