import java.util.Scanner;

/**
 * Created by August DH on 2016-12-15.
 */
public class DifferentDistances {
    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);
        double X1 = 1;
        String printScreen = "";

        while(X1 != 0){

            String input = sc.nextLine();
            String[] splittedInput = input.split(" ");
            X1 = Double.parseDouble((splittedInput[0]));

            if(X1 != 0) {
                double Y1 = Double.parseDouble((splittedInput[1]));
                double X2 = Double.parseDouble((splittedInput[2]));
                double Y2 = Double.parseDouble((splittedInput[3]));
                double p = Double.parseDouble((splittedInput[4]));

                double Xsum = Math.pow(Math.abs(X1 - X2), p);
                double Ysum =(Math.pow(Math.abs(Y1 - Y2), p));

                double sum = Math.pow(((Xsum) + (Ysum)), (1/p));

                printScreen += sum + "\n";
            }
        }

        System.out.print(printScreen);
    }
}
