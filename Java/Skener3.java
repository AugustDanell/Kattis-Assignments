import java.util.Scanner;

/**
 * Created by August DH on 2017-06-21.
 */
public class Skener3 {
    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);
        StringBuilder builder = new StringBuilder();

        String input = sc.nextLine();
        String[] splitted = input.split(" ");

        int rows = Integer.parseInt(splitted[0]);
        int columns = Integer.parseInt(splitted[1]);

        String[] rowArray = new String[rows];

        int Zr = Integer.parseInt(splitted[2]);
        int Zc = Integer.parseInt(splitted[3]);

        for(int i = 0; i < rows; i++){
            String rowInput = sc.nextLine();
            rowArray[i] = rowInput;
        }

        for(int i = 0; i < rows * Zr; i++){
            for(int j = 0; j < columns * Zc; j++){
                builder.append(rowArray[i/Zr].charAt(j/Zc));
            }
            builder.append("\n");
        }

        System.out.print(builder.toString());
    }
}
