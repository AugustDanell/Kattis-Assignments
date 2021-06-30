import java.util.Arrays;
import java.util.Scanner;

/**
 * Created by August DH on 2016-12-10.
 */
public class Modulo {
    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);
        int[] inputedValues = new int[10];
        int[] processedValues = new int[10];
        int[] distinctValues = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
        boolean[] isAlreadyCounted = new boolean[10];
        boolean[] isAlreadyFalse = new boolean[10];
        for(int i = 0; i<10; i++){
            isAlreadyCounted[i] = false;
            isAlreadyFalse[i] = false;
        }

        for (int i =0; i < 10; i++){
            inputedValues[i] = sc.nextInt();
            if(inputedValues[i] > 999){
                inputedValues[i] = 999;
            }
            if(inputedValues[i] < 0){
                inputedValues[i] += 2*inputedValues[i];
            }
            processedValues[i] = inputedValues[i] % 42;
        }
       //System.out.println(Arrays.toString(processedValues));
        for(int i = 0; i < 10; i++){
            for(int j = 0; j < 10; j++){
                if(processedValues[i] != processedValues[j] && i != j && !isAlreadyFalse[i]){
                    distinctValues[i] = 1;
                }
                if(processedValues[i] == processedValues[j] && i != j && !isAlreadyCounted[i]){
                    distinctValues[i] = 1;
                    isAlreadyCounted[j] = true;
                    isAlreadyFalse[i] = true;
                    isAlreadyFalse[j] = true;
                }
            }
        }

        int sum = 0;
        for(int i = 0; i < 10; i++){
            sum +=distinctValues[i];
        }

        if(sum != 11) {
            System.out.println(sum);
        }
    }
}
