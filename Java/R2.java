import java.util.Scanner;

/**
 * Created by August DH on 2017-03-30.
 */
public class R2 {
    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);
        String input = sc.nextLine();
        String[] splitted = input.split(" ");

        int R1 = Integer.parseInt(splitted[0]);
        int mean = Integer.parseInt(splitted[1]);

        int R2 = 0;
        while(R1 + R2 < 2*mean){
            R2++;
        }
        while(R1 + R2 > 2*mean){
            R2--;
        }
        System.out.print(R2);
    }
}
