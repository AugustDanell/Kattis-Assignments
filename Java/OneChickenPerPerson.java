import java.util.Scanner;

/**
 * Created by August DH on 2017-03-30.
 */
public class OneChickenPerPerson {
    public static void main(String[]args) {
        Scanner sc = new Scanner(System.in);
        String input = sc.nextLine();
        String[] splitted = input.split(" ");

        int n = Integer.parseInt(splitted[0]);
        int m = Integer.parseInt(splitted[1]);

        if ((m - n) > 0) {
            if((m-n) == 1){
                System.out.print("Dr. Chaz will have 1 piece of chicken left over!");
            }
            else{
                System.out.print("Dr. Chaz will have " + (m-n) + " pieces of chicken left over!");
            }
        }
        if((m-n) < 0){
            if((m-n) == -1){
                System.out.print("Dr. Chaz needs 1 more piece of chicken!");
            }
            else{
                System.out.print("Dr. Chaz needs "+ (n-m) + " more pieces of chicken!");
            }
        }
    }
}
