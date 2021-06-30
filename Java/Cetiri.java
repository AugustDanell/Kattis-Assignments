import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

/**
 * Created by August DH on 2017-02-05.
 */
public class Cetiri {
    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);
        String input = sc.nextLine();
        String[] splittedInput = input.split(" ");
        ArrayList<Integer> sortingList = new ArrayList<>();

        int integerOne = Integer.parseInt(splittedInput[0]);
        int integerTwo = Integer.parseInt(splittedInput[1]);
        int integerThree = Integer.parseInt(splittedInput[2]);

        int integerFour = 0;

        //If the partial sequence is continous
        if((integerTwo - integerOne) == (integerThree - integerTwo)){
            integerFour = integerThree + (integerTwo-integerOne);

        }
        //If the partial sequence is not continous.
        else{
            sortingList.add(integerOne); sortingList.add(integerTwo); sortingList.add(integerThree);
            Collections.sort(sortingList);

            //Acquiring the difference between the ints
            int difference = sortingList.get(1) - sortingList.get(0);
            if(difference > (sortingList.get(2) - sortingList.get(1))){
                difference = sortingList.get(2) - sortingList.get(1);
            }

            int guessedInt[] = new int[3];
            guessedInt[0] = sortingList.get(0) + difference;
            guessedInt[1] = sortingList.get(0) + 2*difference;
            guessedInt[2] = sortingList.get(0) + 3*difference;

            for(int i = 0; i < 3; i++){
                if(!sortingList.contains(guessedInt[i])){
                    integerFour = guessedInt[i];
                }
            }
        }

        //Printing the last integer
        System.out.print(integerFour);
    }
}
