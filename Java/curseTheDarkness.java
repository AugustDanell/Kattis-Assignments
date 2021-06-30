import java.util.Scanner;
import java.lang.*;
/**
 * Created by August DH on 2017-04-13.
 */
public class curseTheDarkness {
    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);
        int tests = sc.nextInt();
        sc.nextLine();
        StringBuilder builderBob = new StringBuilder();


        for(int i = 0; i < tests; i++){
            String bookInput = sc.nextLine();
            String[] splittedBook = bookInput.split(" ");
            double x = Double.parseDouble(splittedBook[0]);
            double y = Double.parseDouble(splittedBook[1]);

            int candles = sc.nextInt();
            sc.nextLine();

            boolean curseTheDarkness = true;
            for(int j = 0; j < candles; j++){
                String candleData = sc.nextLine();
                String[] splittedCandle = candleData.split(" ");
                double cX = Double.parseDouble(splittedCandle[0]);
                double cY = Double.parseDouble(splittedCandle[1]);

                double dX = Math.pow((cX-x), 2);
                double dY = Math.pow((cY - y),2);

                double distance = Math.sqrt(dX + dY);
                if(distance < 8){
                    curseTheDarkness = false;
                }
            }

            if(curseTheDarkness){
                builderBob.append("curse the darkness\n");
            }
            else{
                builderBob.append("light a candle\n");
            }
        }

        System.out.print(builderBob.toString());
    }
}
