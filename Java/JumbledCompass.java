import java.util.Scanner;

/**
 * Created by August DH on 2016-12-13.
 */
public class JumbledCompass {
    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);

        String input = sc.nextLine();
        String[] splittedChange = input.split(" ");
        int change = Integer.parseInt(splittedChange[0]);

        input = sc.nextLine();
        String[] splittedDegree = input.split(" ");
        int degree = Integer.parseInt(splittedDegree[0]);

        int sum = (degree - change)%360;

        if(sum%360>180){
            sum -= 360;
        }
        if(sum%360 < -180){
            sum += 360;
        }

        if(sum == -180){
            sum = 180;

        }

        System.out.println(sum);
    }
}
