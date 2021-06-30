import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

/**
 * Created by August DH on 2016-12-19.
 */
public class Prva {
    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);
        String caseInput = sc.nextLine();
        String[] splittedCaseInput = caseInput.split(" ");
        ArrayList<String> wordList = new ArrayList<>();

        int R = Integer.parseInt(splittedCaseInput[0]);
        int C = Integer.parseInt(splittedCaseInput[1]);

        String board[] = new String[R];

        for(int i = 0; i < R; i++){
            board[i] = "";
        }

        for(int i = 1; i<= R; i++){
            String input = sc.nextLine();
            board[i-1] += input;
            if(i != R){
                //board[i-1] += "\n";
            }

            String[] splittedRow = input.split("#");
            for(int j = 0; j < splittedRow.length; j++){
                if(splittedRow[j].length() >= 2){
                    wordList.add(splittedRow[j]);
                }
            }

        }

        for(int i = 0; i < C; i++){
            String column = "";
            for(int j = 0; j < R; j++){
                column+= "" + board[j].charAt(i);
            }
            //System.out.print(column + "\n"); //Funkar
            String[] splittedColumns = column.split("#");

            for(int k = 0; k < splittedColumns.length; k++){
                if(splittedColumns[k].length() >= 2){
                    wordList.add(splittedColumns[k]);
                }
            }
        }
        Collections.sort(wordList);
        System.out.println(wordList.get(0));
    }
}
