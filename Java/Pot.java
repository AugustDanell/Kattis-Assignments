import java.util.Scanner;

/**
 * Created by August DH on 2016-12-09.
 */
public class Pot {
    public static void main(String[]args){
        int sum = 0;
        int [] inputedValues = new int[10];
        int rows;

        Scanner scan = new Scanner(System.in);
        rows = scan.nextInt();

        while(rows > 0){
            inputedValues[rows] = scan.nextInt();
            sum += Math.pow((inputedValues[rows]/10), (inputedValues[rows]%10));
            rows--;
        }

        System.out.println(sum);

    }
}
