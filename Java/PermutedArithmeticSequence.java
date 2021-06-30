import java.util.Arrays;
import java.util.Scanner;

/**
 * Created by August DH on 2016-12-15.
 */
public class PermutedArithmeticSequence {

    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);

        String sequenceInput = sc.nextLine();
        String[] splittedSequenceInput = sequenceInput.split(" ");
        int sequences = Integer.parseInt( splittedSequenceInput[0]);
        String returnString = "";


        for(int i = 0; i<sequences; i++){
            boolean arithmetic = true;
            boolean permutated = true;
            boolean nonArithmetic = false;

            String input = sc.nextLine();
            String[] splittedInput = input.split(" ");
            int numberOfArithmeticSequences = Integer.parseInt(splittedInput[0]);
            int[] arithmeticSequences = new int[numberOfArithmeticSequences];

            //Filling the arithmeticSequences array with ints
            for(int j = 0; j<numberOfArithmeticSequences; j++){
                arithmeticSequences[j] = Integer.parseInt(splittedInput[j+1]);
            }

            //System.out.println(Arrays.toString(arithmeticSequences));

            for(int j = 0; j<numberOfArithmeticSequences-2; j++){
                if ((arithmeticSequences[j+2]-arithmeticSequences[j+1]) != (arithmeticSequences[j+1] - arithmeticSequences[j])){
                    arithmetic = false;

                }
            }

            //Implementing an insertion sort upon the array, given that it isn't strictly arithmetic.
            for(int j = 1; j<arithmeticSequences.length; j++){
                int X = arithmeticSequences[j];
                int k = j-1;
                while(k >= 0 && arithmeticSequences[k] > X){
                    arithmeticSequences[k+1] = arithmeticSequences[k];
                    k--;
                }
                arithmeticSequences[k+1] = X;
            }

            //System.out.println(Arrays.toString(arithmeticSequences));

            for(int j = 0; j<numberOfArithmeticSequences-2; j++){
                if ((arithmeticSequences[j+2]-arithmeticSequences[j+1]) != (arithmeticSequences[j+1] - arithmeticSequences[j]) && !arithmetic){
                    permutated = false;
                }
            }

            if(!permutated && !arithmetic){
                nonArithmetic = true;
            }

            if(arithmetic){
                returnString += "arithmetic" + "\n";
            }
            else if(permutated){
                returnString += "permuted arithmetic" + "\n";
            }

            if(nonArithmetic){
                returnString += "non-arithmetic" + "\n";
            }
        }

        System.out.println(returnString);
    }

}
