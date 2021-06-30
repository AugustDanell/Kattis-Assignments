import java.util.Arrays;
import java.util.Scanner;

/**
 * Created by August DH on 2016-12-09.
 */

public class Cetvrta {
    boolean sequentialSearch(int[] array, int searchedElement){
        int sizeOfArray = array.length;
        boolean returnIndex = false;

        for(int i = 0; i<sizeOfArray; i++){
            if(searchedElement == array[i]){
                returnIndex = true;
            }
        }

        return returnIndex;
    }

    public static void main(String[]args){
        Cetvrta test = new Cetvrta();

        Scanner sc = new Scanner(System.in);
        String[] input = new String[10];
        String[] splittedString = new String [10];
        int[] corner = new int[2];
        int[] intArray = new int[6];


        input[0] = sc.nextLine();
        input[1] = sc.nextLine();
        input[2] = sc.nextLine();

        splittedString = input[0].split(" ");
        intArray[0] = Integer.parseInt(splittedString[0]);
        intArray[1] = Integer.parseInt((splittedString[1]));
        //System.out.println(Arrays.toString(splittedString));

        splittedString = input[1].split(" ");
        intArray[2] = Integer.parseInt(splittedString[0]);
        intArray[3] = Integer.parseInt((splittedString[1]));
        //System.out.println(Arrays.toString(splittedString));

        splittedString = input[2].split(" ");
        intArray[4] = Integer.parseInt(splittedString[0]);
        intArray[5] = Integer.parseInt(splittedString[1]);
        //System.out.println(Arrays.toString(splittedString));


        int[] splitIntArray = {intArray[2], intArray[3], intArray[4], intArray[5]};
        if(test.sequentialSearch(splitIntArray, intArray[0]) && test.sequentialSearch(splitIntArray, intArray[1])){

        }

        int[] splitIntArray2 = {intArray[0], intArray[1], intArray[4], intArray[5]};
        if(test.sequentialSearch(splitIntArray, intArray[2]) && test.sequentialSearch(splitIntArray, intArray[3])){

        }

        int[] splitIntArray3 = {intArray[0], intArray[1], intArray[2], intArray[3]};
        if(test.sequentialSearch(splitIntArray, intArray[4]) && test.sequentialSearch(splitIntArray, intArray[5])){

        }

        //System.out.println(Arrays.toString(intArray));
        int[] xArray = {intArray[0], intArray[2], intArray[4]};
        int[] yArray = {intArray[1], intArray[3], intArray[5]};

        int searchedForXValue = 0;
        if(intArray[0]!=intArray[2] && intArray[0] != intArray[4]){
            searchedForXValue = intArray[0];
        }
        if(intArray[2]!=intArray[0] && intArray[2] != intArray[4]){
            searchedForXValue = intArray[2];
        }
        if(intArray[4]!=intArray[2] && intArray[4] != intArray[0]){
            searchedForXValue = intArray[4];
        }

        int searchedForYValue = 0;
        if(intArray[1]!=intArray[3] && intArray[1] != intArray[5]){
            searchedForYValue = intArray[1];
        }
        if(intArray[3]!=intArray[1] && intArray[3] != intArray[5]){
            searchedForYValue = intArray[3];
        }
        if(intArray[5]!=intArray[3] && intArray[5] != intArray[1]){
            searchedForYValue = intArray[5];
        }

        System.out.println(searchedForXValue + " " + searchedForYValue);
    }

}
