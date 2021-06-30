import java.util.Scanner;

/**
 * Created by August DH on 2017-06-14.
 */
public class putovanje2 {
    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);
        String input = sc.nextLine();
        String[] splittedInput = input.split(" ");

        int N = Integer.parseInt(splittedInput[0]);
        int C = Integer.parseInt(splittedInput[1]);

        String fruitStack = sc.nextLine();
        String[] splittedFruitStack = fruitStack.split(" ");
        int maxFruits = 0;

        for(int i = 0; i < splittedFruitStack.length; i++){
            int fruits = 0;
            int eaten = 0;

            for(int j = i; j < splittedFruitStack.length; j++){
                int fruit = Integer.parseInt(splittedFruitStack[j]);
                if(eaten + fruit <= C){
                    eaten += fruit;
                    fruits ++;
                }
                else{
                    //break;
                }
            }

            if(fruits > maxFruits){
                maxFruits = fruits;
            }
        }

        System.out.print(maxFruits);
    }
}
