import java.util.Scanner;

/**
 * Created by August DH on 2016-12-18.
 */
public class Parking {
    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);
        String costInput = sc.nextLine();
        String[] splittedCostInput = costInput.split(" ");

        int A = Integer.parseInt(splittedCostInput[0]);
        int B = Integer.parseInt(splittedCostInput[1]);
        int C = Integer.parseInt(splittedCostInput[2]);

        int minValue = 0;
        int maxValue = 0;

        //Booleans used to find a min and max value, so that the cost-loop can be done correctly.
        boolean[] max = new boolean[3];
        boolean[] min = new boolean[3];

        //Initializing booleans later used
        for(int i = 0; i < 3; i++){
            max[i] = true;
            min[i] = true;
        }

        int [] arrivals = new int[3];
        int [] departures = new int[3];


        //Inputing the arrival and departure data
        for(int i = 0; i < 3; i++){
            String truckInput = sc.nextLine();
            String[] splittedTruckInput = truckInput.split(" ");

            int arrival = Integer.parseInt(splittedTruckInput[0]);
            int departure = Integer.parseInt(splittedTruckInput[1]);

            arrivals[i] = arrival;
            departures[i] = departure;
        }

        for(int i = 0; i < 3; i++){
            for(int j = 0; j < 3; j++){
                if(i!= j && arrivals[i] > arrivals[j] ){
                    min[i] = false;
                }

                if(i!=j && departures[i] < departures[j] ){
                    max[i] = false;
                }
            }
        }

        for(int i = 0; i < 3; i++){
            if(max[i]){
                maxValue = departures[i];
            }

            if(min[i]){
                minValue = arrivals[i];
            }
        }

        int TruckA = 0;
        int TruckB = 0;
        int TruckC = 0;

        int sum = 0;
        for (int i = minValue; i < maxValue; i++){
            TruckA = 0;
            TruckB = 0;
            TruckC = 0;

            if(i >= arrivals[0] && i < departures[0]){
                TruckA = 1;
            }

            if(i >= arrivals[1] && i < departures[1]){
                TruckB = 1;
            }

            if( i >= arrivals[2] && i < departures [2]){
                TruckC = 1;
            }

            int trucksParked = TruckA + TruckB + TruckC;

            if(trucksParked == 3){
                sum += (3* C);
            }

            if(trucksParked == 2){
                sum += (2*B);
            }

            if(trucksParked == 1){
                sum += A;
            }


        }

        System.out.print(sum);
    }
}
