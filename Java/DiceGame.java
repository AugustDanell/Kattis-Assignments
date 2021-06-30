import java.util.Scanner;

/**
 * Created by August DH on 2016-12-17.
 */
public class DiceGame {
    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);

        String GunnarInput = sc.nextLine();
        String EmmaInput = sc.nextLine();

        String[] splittedGunnarInput = GunnarInput.split(" ");
        String[] splittedEmmaInput = EmmaInput.split(" ");

        int gunnarA1 = Integer.parseInt(splittedGunnarInput[0]);
        int gunnarA2 = Integer.parseInt(splittedGunnarInput[1]);
        int gunnarB1 = Integer.parseInt(splittedGunnarInput[2]);
        int gunnarB2 = Integer.parseInt(splittedGunnarInput[3]);

        double gunnarChanceOfEachOutcomeOfFirstDie = 1/(gunnarA2 - gunnarA1 +1);
        double gunnarChanceOfEachOutcomeSecondDie  = 1/(gunnarB2 - gunnarB1 +1);

        double gunnarEachCase[] = new double[(gunnarA2 - gunnarA1 +1) + (gunnarB2 - gunnarB1 +1)];


        int emmaA1 = Integer.parseInt(splittedEmmaInput[0]);
        int emmaA2 = Integer.parseInt(splittedEmmaInput[1]);
        int emmaB1 = Integer.parseInt(splittedEmmaInput[2]);
        int emmaB2 = Integer.parseInt(splittedEmmaInput[3]);

       /* double emmaChanceOfEachOutcome = 1/(emmaA2 - emmaA1 +1);
        double emmaChanceOfEachOutcomeSecondDie = 1/(emmaB2 - emmaB1 +1);
        */

       float emmaProbability = (float)(emmaA1 + emmaA2)/2 + (float)(emmaB1 + emmaB2)/2;
       float gunnarProbability = (float)(gunnarA1 + gunnarA2)/2 + (float)(gunnarB1 + gunnarB2)/2;
       //System.out.print(emmaProbability);
       if(emmaProbability > gunnarProbability){
           System.out.println("Emma");
       }
       else if (gunnarProbability > emmaProbability){
           System.out.println("Gunnar");
       }
       else{
           System.out.println("Tie");
       }
    }
}
