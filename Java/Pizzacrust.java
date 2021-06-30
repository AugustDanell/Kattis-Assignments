import java.util.Scanner;

/**
 * Created by August DH on 2016-12-11.
 */
public class Pizzacrust {
    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);
        String input = sc.nextLine();
        String[] splittedString = new String[2];
        splittedString = input.split(" ");

        //Parsing the input
        int[] ints = new int[2];
        ints [0] = Integer.parseInt(splittedString[0]);
        ints [1] = Integer.parseInt(splittedString[1]);

        //Calculating
        double totalPizzaSize = Math.PI * ints[0] * ints[0];
        double crustedPizza =  Math.PI*ints[0] * ints[0] - (Math.PI * (ints[0]-ints[1]) * (ints[0]-ints[1]));
        double cheesedPart = totalPizzaSize - crustedPizza;

        if(ints[0] < ints[1]){
            System.out.println("0.000000000");
        }
        else {
            System.out.println((cheesedPart / totalPizzaSize) * 100.000000);
        }
    }
}
