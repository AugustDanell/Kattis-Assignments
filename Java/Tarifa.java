import java.util.Scanner;

/**
 * Created by August DH on 2017-03-30.
 * Problem ID: Tarifa
 */
public class Tarifa {
    public static void main(String[]args){
        Scanner sc = new Scanner (System.in);
        int megatbytes = sc.nextInt();
        sc.nextLine();

        int months = sc.nextInt();
        sc.nextLine();

        int available = megatbytes;
        for(int i = 0; i < months; i++){
            int usedMegabytes = sc.nextInt();
            sc.nextLine();

            available += megatbytes - usedMegabytes;
        }

        System.out.print(available);
    }
}
