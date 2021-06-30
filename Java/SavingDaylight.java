import java.util.Scanner;

/**
 * Created by August DH on 2016-12-14.
 */
public class SavingDaylight {
    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);
        String input = sc.nextLine();
        StringBuilder builderBob = new StringBuilder();

        int i = 0;
        while(sc.hasNextLine()){
            if(i != 0){
                input = sc.nextLine();
            }
            String[] splittedInput = input.split(" ");
            String[] splittedFirstTime = splittedInput[3].split(":");
            int FirstTimeHours = Integer.parseInt(splittedFirstTime[0]);
            int FirstTimeMinutes = Integer.parseInt(splittedFirstTime[1]);
            String[] splittedSecondTime = splittedInput[4].split(":");
            int SecondTimeHours = Integer.parseInt(splittedSecondTime[0]);
            int SecondTimeMinutes = Integer.parseInt(splittedSecondTime[1]);

            int totalHours = SecondTimeHours - FirstTimeHours;
            int totalMinutes = SecondTimeMinutes - FirstTimeMinutes;

            if(totalMinutes < 0){
                totalHours --;
                totalMinutes += 60;
            }

            builderBob.append(splittedInput[0] + " " + splittedInput[1] + " " + splittedInput[2] + " " + totalHours + " hours " + totalMinutes + " minutes");
            i++;
            builderBob.append("\n");
        }

        System.out.print(builderBob.toString());
    }
}
