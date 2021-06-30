import java.util.Scanner;

/**
 * Created by August DH on 2017-08-07.
 * Solution to: Growling Gears
 */
public class GG {
    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);
        StringBuilder builder = new StringBuilder();

        int tests = sc.nextInt();
        sc.nextLine();

        for(int i = 0; i < tests; i++){
            int gears = sc.nextInt();
            sc.nextLine();

            double Max = 0;
            int index = 0;
            for(int j = 0; j < gears; j++){
                String gear = sc.nextLine();
                String[] splitted = gear.split(" ");

                double a = Double.parseDouble(splitted[0]);
                double b = Double.parseDouble(splitted[1]);
                double c = Double.parseDouble(splitted[2]);

                double maxX = ((b)/ (2*a)); //Double minus negation
                //System.out.println(maxX);
                double current = -a*Math.pow(maxX, 2) + b*maxX + c;

                //System.out.println(current);
                if(current > Max){
                    index = j+1;
                    Max = current;
                }
            }
            builder.append(index + "\n");
        }

        System.out.print(builder.toString());
    }
}
