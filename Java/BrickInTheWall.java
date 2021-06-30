import java.util.Scanner;

/**
 * Created by August DH on 2017-02-18.
 */
public class BrickInTheWall {
    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);
        StringBuilder builder = new StringBuilder();

        String input = sc.nextLine();
        String[] splittedInput = input.split(" ");

        int h = Integer.parseInt(splittedInput[0]);
        int w = Integer.parseInt(splittedInput[1]);
        int n = Integer.parseInt(splittedInput[2]);

        String brickInput = sc.nextLine();
        String[] splittedBrickInput = brickInput.split(" ");

        int sum = 0;
        boolean Leave = false;
        for(int i = 0; i < n; i++){
            //System.out.println(sum + Integer.parseInt(splittedBrickInput[i]));
            if(sum + Integer.parseInt(splittedBrickInput[i]) > w){
                Leave = true;
            }

            sum = (sum + Integer.parseInt(splittedBrickInput[i])) % w;
        }

        if(!Leave){
            builder.append("YES");
        }
        else{
            builder.append("NO");
        }

        System.out.print(builder.toString());
    }
}
