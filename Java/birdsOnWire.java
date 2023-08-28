/**
 * Birds On A Wire
 * A surprisingly difficult problem, my 744th kattis: https://open.kattis.com/problems/birds
 *
 * General Solution:
 * The general solution to this problem is to fit two birds, if possible, at the very ends of the poles. Now we have
 * an optimal solution for maximum of 2 additional birds. What we can do herenext is to iterate over every adjacent
 * pair of birds. We take the space between them and see if any new birds can be fitted. The formula for checking that
 * is: (residual - d) / d. The idea is that if we can fit x birds, then there will be x+1 spaces, all of a distance of
 * d, where the residual is the total distance between two birds. 
 */

import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;
public class birdsOnWire {
    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);
        String input[] = sc.nextLine().split(" ");
        int l = Integer.parseInt(input[0]);
        int d = Integer.parseInt(input[1]);
        int n = Integer.parseInt(input[2]);
        ArrayList<Integer> birds = new ArrayList<>();
        for(int i = 0; i < n; i++){
            birds.add(Integer.parseInt(sc.nextLine()));
        }
        Collections.sort(birds);
        // Fit the end birds:
        int counter = 0;
        if(l > 11){
            // Fit the first bird:
            if(birds.size() == 0){
                birds.add(6);
                counter ++;
            }
            else if(birds.get(0) >= 6+d){
                birds.add(0, 6);
                counter ++;
            }


            // Fit the last bird:
            if(birds.get(birds.size()-1) <= l-d-6){
                birds.add(l-6);
                counter ++;
            }
        }

        //System.out.println(birds.toString());
        for(int i = 0; i < birds.size()-1; i++){
            int firstBird = birds.get(i);
            int secondBird = birds.get(i+1);
            int residual = secondBird - firstBird;
            int birdsToFit = (residual-d)/(d);
            counter += birdsToFit;
        }

        System.out.println(counter);
    }
}
