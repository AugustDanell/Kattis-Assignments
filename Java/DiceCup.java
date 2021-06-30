import java.util.Arrays;
import java.util.Scanner;

/**
 * Created by August DH on 2016-12-11.
 */
public class DiceCup {
    public static void main(String[]args){
        //Inputting values
        Scanner sc = new Scanner(System.in);
        String input = sc.nextLine();

        //Parsing the input
        String[] splittedString = input.split(" ");
        int[] intArray = {Integer.parseInt(splittedString[0]), Integer.parseInt(splittedString[1])};

      //  System.out.println(Arrays.toString(intArray));

        if(intArray[0] > intArray[1]){
            for(int i = intArray[1] + 1; i <= intArray[0]+1; i++){
                System.out.println(i);
            }
        }
        else if(intArray[1] > intArray[0]){
            for(int i = intArray[0] + 1; i <= intArray[1]+1; i++) {
                System.out.println(i);
            }
        }
        else{
            System.out.println(intArray[0]+1);
        }
    }
}
