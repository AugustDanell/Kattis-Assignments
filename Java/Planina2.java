import java.util.Scanner;

/**
 * Created by August DH on 2017-07-16.
 */
public class Planina2 {
    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);
        int input = sc.nextInt();
        sc.nextLine(); //To use up the entire row.

        input = (int)Math.pow(2, input);
        input ++;
        input = (int)Math.pow(input, 2);

        System.out.println(input);
    }
}
