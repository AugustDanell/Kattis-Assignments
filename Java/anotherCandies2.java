import java.math.BigInteger;
import java.util.Scanner;

/**
 * Created by August DH on 2017-03-07.
 */
public class anotherCandies2 {
    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);
        StringBuilder builder = new StringBuilder();

        int cases = sc.nextInt();
        sc.nextLine();

        for(int i  = 0; i < cases; i++){
            String blankspace = sc.nextLine();

            int kids = sc.nextInt();
            sc.nextLine();

            BigInteger bigKid = new BigInteger("" + kids);
            BigInteger candies = new BigInteger("0");
            BigInteger zero = new BigInteger("0");
            for(int j = 0; j < kids; j++){
                long gives = sc.nextLong();
                sc.nextLine();

                BigInteger bigGive = new BigInteger("" + gives);
                candies = candies.add(bigGive);
            }
            if(candies.mod(bigKid).equals(zero)){
                builder.append("YES\n");
            }
            else{
                builder.append("NO\n");
            }
        }

        System.out.print(builder.toString());
    }
}
