import java.util.Arrays;
import java.util.Scanner;

/**
 * Created by August DH on 2016-12-11.
 */
public class FizzBuzz {
    public static void main(String[]args){
        //Input
        Scanner sc = new Scanner(System.in);
        String input = sc.nextLine();

        //Splitting
        String[] splittedString = input.split(" ");

        //Parsing
        int[] intArray = {Integer.parseInt(splittedString[0]),
                          Integer.parseInt(splittedString[1]),
                          Integer.parseInt(splittedString[2])
        };

        //System.out.println(Arrays.toString(intArray));

        //Fills up the interwall
        int[] interwall = new int[intArray[intArray.length-1]];
        for (int i = 0; i < intArray[intArray.length-1]; i++){
                interwall[i] = i +1;
        }

        //System.out.println(Arrays.toString(interwall));

        //Calculates which numbers are dividable with the numbers in the interwall
        String[] returnArrayString = new String[interwall.length];
        for(int i = 0; i<interwall.length; i++){
            returnArrayString[i] = "" +(i+1);
            if((i+1) % intArray[0] == 0){
                returnArrayString[i] = "Fizz";
            }
            else if ((i+1) % intArray[1] == 0){
                returnArrayString[i] = "Buzz";
            }
            if((i+1)% intArray[0] == 0 && (i+1) % intArray[1] == 0){
                returnArrayString[i] = "FizzBuzz";
            }

        }

      //  System.out.println(Arrays.toString(returnArrayString));

        String returnString = "";
        for(int i = 0; i<returnArrayString.length; i++){
            System.out.println(returnArrayString[i]);
        }

    }
}
