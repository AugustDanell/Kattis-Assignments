import java.util.Arrays;
import java.util.Scanner;

/**
 * Created by August DH on 2016-12-10.
 */
public class Bijele {
    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);
        String input = sc.nextLine();
        String[] array = input.split(" ");
        int[] intArray = new int[6];
        int[] gameSetArray = {1, 1, 2, 2, 2, 8};
        String printString = "";

        for(int i = 0; i < 6; i++){
            intArray[i] = Integer.parseInt(array[i]);
            gameSetArray[i] -= intArray[i];
            printString += gameSetArray[i] + " ";
        }


        System.out.println(printString);
       // System.out.println(Arrays.toString(gameSetArray));
    }
}
