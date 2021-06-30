import java.util.Scanner;

/**
 * Created by August DH on 2016-12-21.
 */
public class Server {
    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);
        String input = sc.nextLine();
        String[] splittedInput = input.split(" ");

        int numberOfTasks = Integer.parseInt(splittedInput[0]);
        int minutesUP = Integer.parseInt(splittedInput[1]);

        String timeRequirements = sc.nextLine();
        String[] splittedTimeRequirements = timeRequirements.split(" ");

        int[] times = new int[splittedTimeRequirements.length];
        for(int i = 0; i < splittedTimeRequirements.length; i++){
            times[i] = Integer.parseInt(splittedTimeRequirements[i]);
        }

        int takenTime = 0;
        int completedTasks = 0;
        if(minutesUP > times[0]) {
            takenTime = times[0];
            int index = 1;
            while(index < times.length && minutesUP >= (takenTime + times[completedTasks+1])) {
                index ++;
                completedTasks++;
                takenTime += times[completedTasks];
            }
            completedTasks ++;
        }
    System.out.print(completedTasks);
    }
}
