import java.util.Arrays;
import java.util.Scanner;

/**
 * Created by August DH on 2016-12-09.
 */
public class ColdputerScience {

    public static void main(String[]args) {
        Scanner sc = new Scanner(System.in);
        int numbers = sc.nextInt();
        sc.nextLine();
        String temperature = "";
        String[] array = new String[numbers];
        int[] intArray = new int[numbers];

        //Fixa en-radsinmatning
        temperature = sc.nextLine();
        array = temperature.split(" ");

        //System.out.println(temperature);


        for(int i = 0; i<numbers; i++){
            intArray[i] = Integer.parseInt(array[i]);
        }
        //System.out.println(Arrays.toString(intArray));
        int minusDegreeCount = 0;

        for(int i = 0; i<numbers; i++){
            if(intArray[i] < 0){
                minusDegreeCount ++;
            }
        }

        System.out.println(minusDegreeCount);
    }


}
