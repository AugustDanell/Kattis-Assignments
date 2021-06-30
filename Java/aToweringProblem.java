import java.util.ArrayList;
import java.util.Collections;
import java.util.Random;
import java.util.Scanner;

/**
 * Created by August DH on 2017-08-09.
 */
public class aToweringProblem {
    public static void Order(String[] array){
        //First set
        int A = Integer.parseInt(array[0]);
        int B = Integer.parseInt(array[1]);
        int C = Integer.parseInt(array[2]);

        ArrayList<Integer> intList = new ArrayList<>();
        intList.add(A);
        intList.add(B);
        intList.add(C);
        Collections.sort(intList);

        for(int i = 0; i < 3; i++){
            array[2-i] = "" + intList.get(i);
        }

        //Second set
        int D = Integer.parseInt(array[3]);
        int E = Integer.parseInt(array[4]);
        int F = Integer.parseInt(array[5]);

        ArrayList<Integer> intList2 = new ArrayList<>();
        intList2.add(D);
        intList2.add(E);
        intList2.add(F);
        Collections.sort(intList2);

        for(int i = 0; i < 3; i++){
            array[5-i] = "" + intList2.get(i);
        }
    }

    public static void Initialize(String [] array){
        for(int i = 0; i < array.length; i++){
            array[0] = "";
        }
    }

    public static void print(String[]array){
        Order(array);
        for(int i = 0; i < array.length; i++){
            System.out.print(array[i]);
            if(i!=array.length-1){
                System.out.print(" ");
            }
        }
    }

    public static void Yates(String[]array){
        Random rand = new Random();
        for(int i = array.length - 1; i > 0; i--){
            int index = rand.nextInt(i+1);
            String temp = array[index];
            array[index] = array[i];
            array[i] = temp;
        }
    }
    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);
        String input = sc.nextLine();
        String[] splitted = input.split(" ");

        int heightTOne = Integer.parseInt(splitted[6]);
        int heightTTwo = Integer.parseInt(splitted[7]);

        String towers[] = new String[6];
        Initialize(towers);

        towers [0] = splitted[0];
        towers [1] = splitted[1];
        towers [2] = splitted[2];
        towers [3] = splitted[3];
        towers [4] = splitted[4];
        towers [5] = splitted[5];

        //Idé: Shuffle algoritm - Fisher Yates Algortih
        boolean run = true;
        while(run){
            Yates(towers);

            int A = Integer.parseInt(towers[0]);
            int B = Integer.parseInt(towers[1]);
            int C = Integer.parseInt(towers[2]);

            if(A + B + C == heightTOne){
                run = false;
            }
        }
        print(towers);
    }
}
