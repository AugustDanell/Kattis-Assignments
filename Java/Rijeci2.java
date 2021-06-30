import java.util.Scanner;

/**
 * Created by August DH on 2017-02-07.
 */
public class Rijeci2 {
    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);
        int timesPressed = sc.nextInt();
        sc.nextLine();

        int b = 0; int a = 0;
        if(timesPressed >= 1){
            a = 1;
        }

        for(int i = 1; i < timesPressed; i++){
            int temp = b;
            b = a;
            a = temp + a;
        }

        System.out.print(b + " " + a);
    }
}
