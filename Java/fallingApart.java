import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

public class fallingApart {
    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);
        int Alice = 0;
        int Bob = 0;

        int ints = sc.nextInt();
        sc.nextLine();

        String input = sc.nextLine();

        ArrayList<Integer> List = new ArrayList<>();
        String splitted[] = input.split(" ");

        for(int i = 0; i < ints; i++){
            List.add(Integer.parseInt(splitted[i]));
        }

        Collections.sort(List);
        for(int i = 0; i < ints; i++){
            if(i%2 == 0){
                Alice += List.get(i);
            }
            else{
                Bob += List.get(i);
            }
        }

        if(Bob > Alice){
            int temp = Alice;
            Alice = Bob;
            Bob = temp;
        }

        System.out.println(Alice + " " + Bob);
    }
}
