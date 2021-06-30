import java.util.Scanner;

/**
 * Created by August DH on 2017-06-14.
 */
public class threeDPrintedStatues {
    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        sc.nextLine();

        int minDays = 10001; //Impossible miniumum

        for(int i = 1; i < 10000; i++){
            int days = 0;
            int m = 0;

            int printers = 1;

            while(m < n){
                if(printers < i){
                    printers += printers;
                }
                else{
                    m += printers;
                }

                days++;
            }

            if(days < minDays){
                minDays = days;
            }
        }

        System.out.print(minDays);
    }
}
