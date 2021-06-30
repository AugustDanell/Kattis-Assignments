import java.util.Scanner;

/**
 * Created by August DH on 2017-04-21.
 * Solution to the problem "Daylight Saving Time".
 */
public class DST {
    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);
        StringBuilder builderBob = new StringBuilder();

        int tests = sc.nextInt();
        sc.nextLine();

        for(int i = 0; i < tests; i++){
            String input = sc.nextLine();
            String[] splittedInput = input.split(" ");

            int differance = Integer.parseInt(splittedInput[1]);
            int hours = Integer.parseInt(splittedInput[2]);
            int minutes = Integer.parseInt(splittedInput[3]);

            boolean increment = true;

            if(splittedInput[0].equals("B")){
                increment = false;
            }

            if(increment){
               minutes += differance;
            }
            else{
               minutes -= differance;
            }

            //Time adjustments
            if(minutes >= 60 && minutes < 120){
                minutes -= 60;
                hours++;
            }else if(minutes >= 120){
                minutes -= 120;
                hours += 2;
            }
            //Negative adjustments
            else if(minutes <0 && minutes >= -60){
                minutes += 60;
                hours --;
            }
            else if(minutes < -60){
                minutes += 120;
                hours -= 2;
            }

            //Hour adjustments
            if(hours == 24){
                hours = 0;
            }
            else if(hours == 25){
                hours = 1;
            }
            else if(hours == -1){
                hours = 23;
            }
            else if(hours == -2){
                hours = 22;
            }

            builderBob.append(hours + " " + minutes + "\n");
        }

        System.out.print(builderBob.toString());
    }
}
