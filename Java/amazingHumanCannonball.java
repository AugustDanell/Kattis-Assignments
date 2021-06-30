import java.util.Scanner;

/**
 * Created by August DH on 2017-07-03.
 */
public class amazingHumanCannonball {
    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);
        StringBuilder builder = new StringBuilder();

        int tests = sc.nextInt();
        sc.nextLine();
        for(int i = 0; i < tests; i++){
            String input = sc.nextLine();
            String[] splittedInput = input.split(" ");

            double g = 9.81;
            double initialSpeed = Double.parseDouble(splittedInput[0]);
            double degree = Double.parseDouble(splittedInput[1]);
            double distance = Double.parseDouble(splittedInput[2]);
            double lowerBound = Double.parseDouble(splittedInput[3]);
            double upperBound = Double.parseDouble(splittedInput[4]);

            //X(t) = V0t cos(theta) -> t = X(t)/V0*cos(theta):
            double time = distance / (initialSpeed * Math.cos(Math.toRadians(degree)));

            //Y(t) = V0t sin(theta) - 1/2gt^2:
            double projectileHeight = (initialSpeed * time * Math.sin(Math.toRadians(degree))) - (0.5 * g * (time * time));
            //It did not work when I wrote (1/2) instead of 0.5.

            //System.out.print(projectileHeight);

            //Remember to include + - 1, since there has to be a safety distance by at least one meter according to the assignment.
            if(projectileHeight > (lowerBound + 1) && projectileHeight < (upperBound - 1)){
                builder.append("Safe");
            }
            else{
                builder.append("Not Safe");
            }

            builder.append("\n");
        }

        System.out.print(builder.toString());
    }
}
