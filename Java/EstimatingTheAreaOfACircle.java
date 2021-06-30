import java.util.DoubleSummaryStatistics;
import java.util.Scanner;

/**
 * Created by August DH on 2016-12-17.
 */
public class EstimatingTheAreaOfACircle {
    public static void main(String[]args){
        boolean run = true;
        Scanner sc = new Scanner(System.in);
        StringBuilder builderBob = new StringBuilder();

        while(run) {
            String input = sc.nextLine();
            String[] splittedInput = input.split(" ");

            double R = Double.parseDouble(splittedInput[0]);
            double M = Double.parseDouble(splittedInput[1]);
            double C = Double.parseDouble(splittedInput[2]);

            //Given that the if-statement is fulfilled, the program terminates
            if(R == 0.0 && M == 0.0 && C == 0.0){
                run = false;
            }
            else{
                double AreaOfCircle = R*R*Math.PI;
                double AreaOfSquare = (R+R)*(R+R);

                double EstimatedCircleArea = AreaOfSquare * (C/M);
                builderBob.append(AreaOfCircle + " " + EstimatedCircleArea + "\n");
            }
        }

        System.out.print(builderBob.toString());
    }
}
