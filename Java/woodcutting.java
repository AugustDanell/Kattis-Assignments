// A solution to the problem: https://open.kattis.com/problems/woodcutting

// Idea: 
// Calculate two terms:
// 1. waitSum is a direct sum of the time a customer has to wait. 2- Delay sum is the time for which there is a delay until 
// they can start. The sum of both gives the correct answer, divided by the amount of customers to give E(x), the expected
// wait time:

import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

public class cuttingWood {
    public static void main(String[]args){

        // 1. Input:
        Scanner sc = new Scanner(System.in);
        int testcases = sc.nextInt();
        sc.nextLine();

        for (int i = 0; i < testcases; i++){
            int customers = sc.nextInt();
            sc.nextLine();
            ArrayList<Integer> customerList = new ArrayList<Integer>();

            // 2. Calculate a total for every customer and append it to the list of customers:
            for(int j = 0; j < customers; j++){
                String[] customerData = sc.nextLine().split(" ");
                int blocks = Integer.parseInt(customerData[0]);
                int total = 0;

                for(int k = 0; k < blocks; k++){
                    total += Integer.parseInt(customerData[k+1]);
                }

                customerList.add(total);
            }

            // 3. Sort the list of customers and calculate a total wait sum starting on the fastest, going up:
            Collections.sort(customerList);
            double waitSum = 0;
            double delaySum = 0;
            for(int j = 0; j < customerList.size(); j++){
                waitSum += customerList.get(j);
                delaySum += customerList.get(j)*(customerList.size() - (j+1));
            }
          

            // 4. Output the delaysum + waitsum / |customers| to obtain the expected wait:          
            System.out.println((delaySum+waitSum) / customerList.size());

        }
    }
}
