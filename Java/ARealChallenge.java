import java.math.BigInteger;
import java.util.Scanner;

/**
 * Created by August DH on 2016-12-10.
 */
public class ARealChallenge {
    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);
        String input = sc.nextLine();

        Long Squaremeter = Long.parseLong(input);

        //int Squaremeter = sc.nextInt();
        double Return = Math.sqrt((double)Squaremeter) * 4;

        System.out.println(Return);
    }
}
