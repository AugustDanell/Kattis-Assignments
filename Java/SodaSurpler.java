import java.util.Scanner;

/**
 * Created by August DH on 2017-02-04.
 * Kattis Problem: Soda Slurper.
 */
public class SodaSurpler {
    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);
        String input = sc.nextLine();
        String[] splittedInput = input.split(" ");

        int bottlesDrunk = 0;
        int e = Integer.parseInt(splittedInput[0]);
        int f = Integer.parseInt(splittedInput[1]);
        int c = Integer.parseInt(splittedInput[2]);

        int bottles = e + f;
        while(bottles >= c ){
            bottles -= c;

            bottlesDrunk ++;
            bottles ++;
        }

        System.out.print(bottlesDrunk);

    }
}
