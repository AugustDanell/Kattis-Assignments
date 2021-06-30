import java.util.Scanner;

/**
 * Created by August DH on 2017-07-03.
 */
public class yingAndYangStones {
    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);
        String input = sc.nextLine();

        int black = 0;
        int white = 0;

        for(int i = 0; i < input.length(); i++){
            if(input.charAt(i) == 'B'){
                black ++;
            }
            else{
                white ++;
            }
        }

        if(black == white){
            System.out.println("1");
        }
        else{
            System.out.println("0");
        }
    }
}
