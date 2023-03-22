// A solution to the problem: https://open.kattis.com/problems/color

import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

public class socks {
    public static void main(String[]args){
        // 1. Do input with the scanner object:
        Scanner sc = new Scanner(System.in);
        int S,K,C;
        String[] s = sc.nextLine().split(" ");
        S = Integer.parseInt(s[0]);
        C = Integer.parseInt(s[1]);
        K = Integer.parseInt(s[2]);
        
        // 2. Put every sock into an arraylist:
        String[] socks = sc.nextLine().split(" ");
        ArrayList<Integer> sockList = new ArrayList<>();
        for(int i = 0; i < socks.length; i++){
            sockList.add(Integer.parseInt(socks[i]));
        }
        
        // 3. Sort the arraylist and initiate counters for the current color and amount of machines needed:
        Collections.sort(sockList);
        int machines = 0;
        int currentColor = 0;
        int remainingCapacity = C;
        
        // 4. Iterate over every sock and intiate a new machine if we are on the first index, our capacity is ended or the new sock is too different:
        for(int i = 0; i < sockList.size(); i++){
            int sock = sockList.get(i);
            //System.out.println(sock - currentColor);
            if (i == 0 || remainingCapacity == 0 || (sock - currentColor) > K){
                machines ++;
                currentColor = sock;
                remainingCapacity = C;
            }
            
            // 5. Decrement the capacity for every sock:
            remainingCapacity --;
        }
        
        // 6. Output the amount of used machines:
        System.out.println(machines);
    }
}
