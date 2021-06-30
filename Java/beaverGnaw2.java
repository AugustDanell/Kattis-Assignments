import java.util.Scanner;

/**
 * Created by August DH on 2017-08-09.
 * Solution to Beaver Gnaw
 */
public class beaverGnaw2 {
    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);
        boolean run = true;

        StringBuilder builder = new StringBuilder();

        while(run){
            String input = sc.nextLine();
            if(input.equals("0 0")){
                run = false;
            }
            else{
                String[] splitted = input.split(" ");
                double D = Double.parseDouble(splitted[0]);
                double V = Double.parseDouble(splitted[1]);

                double nV = V * 6;
                double d = Math.pow(Math.pow(D, 3) - (nV/Math.PI), 1.0/3.0);


                builder.append(d + "\n");
            }
        }

        System.out.print(builder.toString());
    }
}
