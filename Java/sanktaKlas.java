import java.util.Scanner;

/**
 * Created by August DH on 2017-08-24.
 */
public class sanktaKlas {
    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);
        String input = sc.nextLine();
        String[] splitted = input.split(" ");

        double H = Double.parseDouble(splitted[0]);
        int V = Integer.parseInt(splitted[1]);

        if(V <= 180){
            System.out.print("safe");
        }
        else{
            double R = Math.toRadians(V);
            double X = ((H/-Math.sin(R)));
            int adjustment = (int)X;

            System.out.print(adjustment);
        }
    }
}
