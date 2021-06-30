import java.util.Scanner;

/**
 * Created by August DH on 2016-12-09.
 */
public class SimonSays {
    public static void main(String[]args) {
        Scanner sc = new Scanner(System.in);
        int rows;
        String input;
        rows = sc.nextInt();
        sc.nextLine();
        String[] savedOutputs = new String[1000];


        for (int i = 0; i<rows; i++){
            input = sc.nextLine();
            //System.out.println(input.length() + input.substring(0,10));
            if(input.length() > 9 && input.substring(0,10).equals("Simon says")){
                savedOutputs[i] = input.substring(10, input.length());
            }
        }

        for (int i = 0; i<rows; i++){
            if(savedOutputs[i] != null) {
                System.out.println(savedOutputs[i]);
            }
        }
    }
}
