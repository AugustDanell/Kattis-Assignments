import java.util.Arrays;
import java.util.Scanner;

/**
 * Created by August DH on 2016-12-12.
 */
public class SpeedLimit {
    public static void main(String[]args){
        boolean run = true;
        Scanner sc = new Scanner(System.in);
        String returnString = "";

        while(run){
            //Input, Splittning and parsning of the first inputed integer
            String input = sc.nextLine();
            String splittedString[] = input.split(" ");
            int rows = Integer.parseInt(splittedString[0]);

            if(rows == -1){
                run = false;
            }

            String inputOfPair;
            if(run){

                int[] totalSpeed = new int[rows];
                int[] totalTime = new int[rows];
                int[] totalDistance = new int[rows];

                //Fills two arrays, totalSpeed and totalTime, with the given speed and time
                for(int i = 0; i < rows; i++) {
                    inputOfPair = sc.nextLine();
                    String[] splittedPair = inputOfPair.split(" ");
                    int speed = Integer.parseInt(splittedPair[0]);
                    int time = Integer.parseInt(splittedPair[1]);

                    totalSpeed[i] = speed;
                    totalTime[i] = time;
                }

                //System.out.println(Arrays.toString(totalSpeed));
                int distanceSum = 0;
                for(int i = 0; i < rows; i++){
                    if(i == 0){
                        totalDistance[i] = totalSpeed[i]*totalTime[i];
                        distanceSum += totalDistance[i];
                    }
                    else{
                        totalDistance[i] = totalSpeed[i]*(totalTime[i]-totalTime[i-1]);
                        distanceSum += totalDistance[i];
                    }
                }
                returnString += "" + distanceSum + " ";
               // System.out.println(returnString);
            }

        }

        String[] returnStrings = returnString.split(" ");

        for(int i = 0; i < returnStrings.length; i++){
            System.out.println(returnStrings[i] + " miles");
        }

    }
}
