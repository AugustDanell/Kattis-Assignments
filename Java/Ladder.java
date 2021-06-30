import java.util.Arrays;
import java.util.Scanner;

/**
 * Created by August DH on 2016-12-11.
 */
public class Ladder {
    public static void main(String[]args){
        //Input
        Scanner sc = new Scanner(System.in);
        String input = sc.nextLine();

        //Splits the input into two substrings
        String[] splitString = new String[2];
        splitString = input.split(" ");

//        System.out.println(Arrays.toString(splitString));

        //Parsing - Parses the substrings into ints
        int[] intArray = new int[2];
        intArray[0] = Integer.parseInt(splitString[0]);
        intArray[1] = Integer.parseInt(splitString[1]);

        //Converts degrees to radians
        double radians = (2*Math.PI*intArray[1])/360;

        double returnValue = intArray[0] / Math.sin(radians);



        System.out.println((int)Math.ceil(returnValue));
    }
}
