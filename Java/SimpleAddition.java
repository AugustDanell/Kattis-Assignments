import java.math.BigInteger;
import java.util.Scanner;

/**
 * Created by August DH on 2016-12-18.
 */
public class SimpleAddition {
    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);
        String firstInteger = sc.nextLine();
        String secondInteger = sc.nextLine();

        String[] splittedFirstInteger = firstInteger.split(" ");
        String[] splittedSecondInteger = secondInteger.split(" ");

        BigInteger IntegerOne = new BigInteger(splittedFirstInteger[0]);
        BigInteger IntegerTwo = new BigInteger(splittedSecondInteger[0]);

        System.out.print(IntegerOne.add(IntegerTwo));
    }
}
