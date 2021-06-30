import java.util.Scanner;

/**
 * Created by August DH on 2016-12-17.
 */
public class GrassSeedInc {
    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);
        String cost = sc.nextLine();
        String[] splittedCost = cost.split(" ");
        double C = Double.parseDouble(splittedCost[0]);

        String lawnsToSow = sc.nextLine();
        String[] splittedLawnsToSow = lawnsToSow.split(" ");
        int L = Integer.parseInt(splittedLawnsToSow[0]);

        double totalCost = 0;
        for(int i = 0; i<L; i++){
            String lawnData = sc.nextLine();
            String[] splittedLawnData = lawnData.split(" ");

            double Width = Double.parseDouble(splittedLawnData [0]);
            double Height = Double.parseDouble(splittedLawnData[1]);

            totalCost += Width*Height*C;
        }


        System.out.print(totalCost);
    }
}
