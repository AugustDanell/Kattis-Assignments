import java.util.ArrayList;
import java.util.Scanner;
public class knights {
    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);
        int n = Integer.parseInt(sc.nextLine());
        ArrayList<ArrayList<Integer>> knightData = new ArrayList<>();
        for(int i = 0; i < n; i++){
            String input[] = sc.nextLine().split(" ");
            int health = Integer.parseInt(input[0]);
            int index = i+1;
            int strength = Integer.parseInt(input[1]);
            ArrayList<Integer> internalData = new ArrayList<>();
            internalData.add(index);
            internalData.add(health);
            internalData.add(strength);
            knightData.add(internalData);
        }


        while(knightData.size() > 1){
            //System.out.println(knightData);
            boolean firstStrike = true;
            boolean kill = false;
            while(!kill){
                if(firstStrike){
                    int remainingHealth = knightData.get(1).get(1) - knightData.get(0).get(2); 
                    knightData.get(1).set(1, remainingHealth);
                    if(remainingHealth <= 0){
                        kill = true;
                        knightData.remove(1);
                    }
                }
                else{
                    int remainingHealth = knightData.get(0).get(1) - knightData.get(1).get(2);
                    knightData.get(0).set(1, remainingHealth);
                    if(remainingHealth <= 0){
                        kill = true;
                        knightData.remove(0);
                    }
                }
                firstStrike = !firstStrike;
            }
        }

        System.out.println(knightData.get(0).get(0));
    }
    
}
