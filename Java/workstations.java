// 742th Kattis: Problem here: https://open.kattis.com/problems/workstations

import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;
public class workstations {
    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);
        String[] split = sc.nextLine().split(" ");
        int n = Integer.parseInt(split[0]);
        int m = Integer.parseInt(split[1]);
        ArrayList<Integer> arrivals = new ArrayList<Integer>();
        ArrayList<Integer> departures = new ArrayList<Integer>();

        for(int i = 0; i < n; i++){
            split = sc.nextLine().split(" ");
            int a = Integer.parseInt(split[0]);
            arrivals.add(a);

            int b = Integer.parseInt(split[1]);
            departures.add(b+a);
        }

        Collections.sort(departures);
        Collections.sort(arrivals);
        int departureCounter = 0;
        int lock_ups = 0;
        for(int arrival : arrivals){
            if(arrival < departures.get(departureCounter)){
                lock_ups ++;
                continue;
            }
            while(arrival > departures.get(departureCounter) + m && departureCounter < departures.size()-1){
                departureCounter ++;
            }
            if(arrival >= departures.get(departureCounter) && arrival <= departures.get(departureCounter) + m){
                departureCounter ++;
                continue;
            }
            else{
                lock_ups ++;
            }
        }

        System.out.println(n-lock_ups);
    }
    
}
