import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

/**
 * Created by August DH on 2017-02-04.
 */
public class Skocimis2 {
    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);
        String input = sc.nextLine();
        String[] splittedInput = input.split(" ");

        ArrayList<Integer> sortingList = new ArrayList<>();

        int kangarooA = Integer.parseInt(splittedInput[0]);
        sortingList.add(kangarooA);

        int kangarooB = Integer.parseInt(splittedInput[1]);
        sortingList.add(kangarooB);

        int kangarooC = Integer.parseInt(splittedInput[2]);
        sortingList.add(kangarooC);

        Collections.sort(sortingList);
        // System.out.print(sortingList);

        if((sortingList.get(1) - sortingList.get(0)) > sortingList.get(2) - sortingList.get(1)){
            System.out.print(sortingList.get(1) - sortingList.get(0) - 1);
        }
        else{
            System.out.print(sortingList.get(2) - sortingList.get(1) - 1);
        }
    }
}
