import java.util.Scanner;

/**
 * Created by August DH on 2017-04-22.
 */
public class impactFactor {
    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);

        String input = sc.nextLine();
        String[] splitted = input.split(" ");

        int articles = Integer.parseInt(splitted[0]);
        int factor = Integer.parseInt(splitted[1]);

        int x = articles * (factor-1) + 1;
        System.out.print(x);
    }
}
