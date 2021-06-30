import java.util.Arrays;
import java.util.Scanner;

/**
 * Created by August DH on 2016-12-11.
 */
public class spavanac {
    public static void main(String[]args){
        //Input
        Scanner sc = new Scanner(System.in);
        String input = sc.nextLine();

        //Splits the string into two substrings
        String[] splittedString = input.split(" ");

        //Parsing
        int[] array = {Integer.parseInt(splittedString [0]), Integer.parseInt(splittedString[1])};

        if(array[1] < 45 ){
            array[0] -= 1;
            if(array[0] == -1){
                array[0] = 23;
            }
        }

        if(array[1] < 45) {
            array[1] = ((array[1] - 45) % 60) + 60;
        }
        else{
            array[1] = array[1] - 45;
        }

        for(int i = 0; i<2; i++) {
            System.out.print(array[i]);
            if(i == 0){
                System.out.print(" ");
            }
        }
    }
}
