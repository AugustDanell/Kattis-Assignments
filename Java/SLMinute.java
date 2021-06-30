import java.util.Scanner;

/**
 * Created by August DH on 2016-12-18.
 * Kattis Problem : Just a Minute.
 */
public class SLMinute {
    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);
        //StringBuilder builderBob = new StringBuilder();

        double SLMinute = 0;
        double totalEstimatedTime = 0;
        double totalWaitedTime = 0;

        String cases = sc.nextLine();
        String[] splittedCases = cases.split(" ");

        int numberOfCases = Integer.parseInt(splittedCases[0]);
        for(int i = 0; i < numberOfCases; i++){
            String input = sc.nextLine();
            String[] splittedInput = input.split(" ");
            double estimatedMinutes = Double.parseDouble(splittedInput[0]);
            double waitedSeconds = Double.parseDouble(splittedInput[1]);

            totalEstimatedTime += estimatedMinutes;
            totalWaitedTime += waitedSeconds;
        }

        SLMinute = totalWaitedTime/(totalEstimatedTime*60);
        if(SLMinute > 1.0) {
            System.out.print(SLMinute);
        }
        else {
            System.out.print("measurement error");
        }

    }
}
