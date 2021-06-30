import java.util.Scanner;

/**
 * Created by August DH on 2017-05-15.
 */
public class Sibicie {
    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);
        StringBuilder builder = new StringBuilder();

        String input = sc.nextLine();
        String[] splittedInput = input.split(" ");

        int matches = Integer.parseInt(splittedInput[0]);
        int width = Integer.parseInt(splittedInput[1]);
        int height = Integer.parseInt(splittedInput[2]);

        int a = width*width + height*height;

        for(int i = 0; i < matches; i++){
            int match = sc.nextInt();
            sc.nextLine();

            if(match * match <= a){
                builder.append("DA\n");
            }
            else{
                builder.append("NE\n");
            }

        }

        System.out.print(builder.toString());
    }
}
