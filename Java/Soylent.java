import java.util.Scanner;

/**
 * Created by August DH on 2016-12-09.
 */
public class Soylent {
public static void main(String[]args){
    int inputedValues[] = new int[1000];
    int processedValues[] = new int[1000];
    Scanner sc = new Scanner(System.in);
    int rows = sc.nextInt();

    for(int i = 0; i < rows; i++){
        inputedValues[i] = sc.nextInt();
        processedValues[i] = (int)Math.ceil (inputedValues[i]/400.0);
    }

    for(int i = 0; i< rows; i++) {
        System.out.println(processedValues[i]);
    }
    }
}
