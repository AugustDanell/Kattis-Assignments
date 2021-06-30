import java.math.BigInteger;
import java.util.Scanner;

/**
 * Created by August DH on 2017-04-11.
 */
public class oktalni2 {
    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);

        String binaryString = sc.nextLine();
        BigInteger decimal = new BigInteger(binaryString, 2);
        System.out.print(decimal.toString(8));

    }
}
