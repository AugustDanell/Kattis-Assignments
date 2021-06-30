import java.util.Scanner;

/**
 * Created by August DH on 2016-12-14.
 */
public class QuickEstimates {
    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);
        String inputOfRows = sc.nextLine();
        String[] splittedString = inputOfRows.split(" ");
        int rows = Integer.parseInt(splittedString[0]);
        String printString = "";

        for (int i = 0; i < rows; i++){
            String input = sc.nextLine();
            printString += input.length() + "\n";

        }

        System.out.print(printString);
    }
}
