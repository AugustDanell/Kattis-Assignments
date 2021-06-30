import java.util.Scanner;
import java.lang.Math;

/**
 * Created by August DH on 2017-02-07.
 */
public class Kornislav {
    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);
        String input = sc.nextLine();
        String[] splittedInput = input.split(" ");

        int distances[] = new int[4];
        distances[0] = Integer.parseInt(splittedInput[0]);
        distances[1] = Integer.parseInt(splittedInput[1]);
        distances[2] = Integer.parseInt(splittedInput[2]);
        distances[3] = Integer.parseInt(splittedInput[3]);

        for(int i = 1; i < 4; i++){
            for(int j = i; j > 0; j--){
                if(distances[j]<distances[j-1]){
                    int temp = distances[j];
                    distances[j] = distances[j-1];
                    distances[j-1] = temp;
                }
            }
        }
        //Now it's sorted!

        int largestArea = 0;

        //Skiter i loopen eftersom det bara är 4 olika
        int area = (Math.min(distances[0], distances[1]) * (Math.min(distances[2], distances[3])));

        if(Math.min(distances[0], distances[2]) * (Math.min(distances[1], distances[3])) > area){
            area = Math.min(distances[0], distances[2]) * (Math.min(distances[1], distances[3]));
        }

        if(Math.min(distances[0], distances[3]) * (Math.min(distances[1], distances[2])) > area){
            area = Math.min(distances[0], distances[3]) * (Math.min(distances[1], distances[2]));
        }

        if(Math.min(distances[1], distances[2]) * (Math.min(distances[0], distances[3])) > area){
            area = Math.min(distances[1], distances[2]) * (Math.min(distances[0], distances[3]));
        }
        if(Math.min(distances[1], distances[3]) * (Math.min(distances[2], distances[0])) > area){
            area = Math.min(distances[0], distances[3]) * (Math.min(distances[2], distances[0]));
        }
        if(Math.min(distances[2], distances[3]) * (Math.min(distances[1], distances[2])) > area){
            area = Math.min(distances[0], distances[1]) * (Math.min(distances[2], distances[3]));
        }

        System.out.print(area);
    }
}
