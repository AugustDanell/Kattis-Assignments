import java.util.Scanner;

/**
 * Created by August DH on 2017-04-06.
 */
public class candleBox {
    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);

        int ageDifferance = sc.nextInt();
        sc.nextLine();

        int candlesRita = sc.nextInt();
        sc.nextLine();

        int candlesTheo = sc.nextInt();
        sc.nextLine();

        int rita = 0;
        int theo = 0;

        boolean theoIsThree = false;
        int counterTheo = 0;
        int counterRita = 0;
        while(theo+rita != candlesRita + candlesTheo){
            rita += (4 + counterRita);
            counterRita ++;
            ageDifferance --; //The actual age differance does of course not decrease.

            if(ageDifferance == 0){
                theoIsThree = true;
            }

            if(theoIsThree) {
                theo += (3 + counterTheo);
                counterTheo++;
            }

        }

        //System.out.print(rita + " " + theo);
        System.out.print(theo - candlesTheo);
    }
}
