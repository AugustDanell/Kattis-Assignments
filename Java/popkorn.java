import java.math.BigInteger;
import java.util.Scanner;

public class popkorn {
    public static void main(String[]args){
        // 1. Take in input, the big Integer object can parse a string:
        Scanner sc = new Scanner(System.in);
        BigInteger N = new BigInteger(sc.nextLine());

        // 2. We have 4 groups consisting of V = n/4 contestants. They form a complete graph.
        BigInteger V = N.divide(new BigInteger("4"));

        // 3. |E| = (V)(V-1)/2. We have four groups, so as a shortcut we multiply E with 2 (since 4/2 = 2):
        BigInteger E = V.multiply(V.subtract(new BigInteger("1")));
        E = E.multiply(new BigInteger("2"));

        // 4. Now add 4 for semifinals, bronze match and final, and print:
        System.out.println(new BigInteger("4").add(E));
    }
}
