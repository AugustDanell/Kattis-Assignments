// 743th Kattis, Problem Description Here: https://open.kattis.com/problems/colorland
/*
General Solution:
A solutions to this problem would be to traverse a counting array, initialized as [-1..]*n, backwards.
Every time a color is shown, we update the array and save that specific instance of the array into a hashmap (using shallow copy).
In this way we can basically create a map that gives us the cost for every next move, at any step on the board.
With this map we can easily do a greedy solution, just jump as far as we can for every step.
We have a counter that counts the amount of steps this would take. 
*/

import java.util.Arrays;
import java.util.HashMap;
import java.util.Scanner;

public class colorland {

    // Order: Blue Orange Pink Green Red Yellow:
    public static HashMap<Integer, Integer[]> backwardsPathing(String[] arrSeq){
        HashMap<Integer, Integer[]> pathMap = new HashMap();
        Integer[] lastArray = {Integer.valueOf(-1), Integer.valueOf(-1), Integer.valueOf(-1), Integer.valueOf(-1), Integer.valueOf(-1), Integer.valueOf(-1)};
        for(int i = arrSeq.length-1; i >= -1; i--){

            // Shallow copy:
            Integer[] occArray = new Integer[6];
            for(int j = 0; j < lastArray.length; j++){
                occArray[j] = Integer.valueOf(lastArray[j]);
            }
            Integer[] insertArray = new Integer[6];
            for(int j = 0; j < lastArray.length; j++){
                insertArray[j] = Integer.valueOf(lastArray[j]);
            }
            pathMap.put(i, insertArray);

            if(i == -1){
                break;
            }

            // Update occurance of the color we are currently indexed on:
            String currentColor = arrSeq[i];
            Integer currentIndex = Integer.valueOf(i);
            if(currentColor.equals("Blue")){
                occArray[0] = currentIndex;
            }
            else if(currentColor.equals("Orange")){
                occArray[1] = currentIndex;
            }
            else if(currentColor.equals("Pink")){
                occArray[2] = currentIndex;
            }
            else if(currentColor.equals("Green")){
                occArray[3] = currentIndex;
            }
            else if(currentColor.equals("Red")){
                occArray[4] = currentIndex;
            }
            else if(currentColor.equals("Yellow")){
                occArray[5] = currentIndex;
            }

            // Pass the array to next iteration:
            for(int j = 0; j < occArray.length; j++){
                lastArray[j] = Integer.valueOf(occArray[j]);
            }
        }
        return pathMap;
    }

    public static int getMaxFromArr(Integer[]arr){
        int max = 0;
        for(int i = 0; i < arr.length; i++){
            int nextSquare = (int)arr[i];
            if (nextSquare > max)
                max = nextSquare;
        }
        return max;
    }

    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);
        int colors = Integer.parseInt(sc.nextLine());
        int current = -1;
        String[] arrSeq = new String[colors];
        
        for(int i = 0; i < colors; i++){
            arrSeq[i] = sc.nextLine();
        }

        HashMap<Integer, Integer[]> map = backwardsPathing(arrSeq);
        int jumps = 0;

        while(current < colors-1){
            current = getMaxFromArr(map.get(current));
            jumps ++;
        }
        System.out.println(jumps);
    }
}
