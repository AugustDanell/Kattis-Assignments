import java.util.Arrays;
import java.util.Scanner;

/**
 * Created by August DH on 2016-12-13.
 */
public class Karte {
    public static void main(String []args){
        Scanner sc = new Scanner(System.in);
        String input = sc.nextLine();
        String returnString = "";

        int Psuit = 13;
        int Ksuit = 13;
        int Hsuit = 13;
        int Tsuit = 13;

        //Takes care of the missing Karte
        for(int i = 0; i < input.length(); i++){
            if((int)input.charAt(i) == 72){
                Hsuit --;
            }
            if((int)input.charAt(i) == 80){
                Psuit --;
            }
            if((int)input.charAt(i) == 84){
                Tsuit --;
            }
            if((int)input.charAt(i) == 75){
                Ksuit--;
            }
        }

        returnString = "" + Psuit + " " + Ksuit + " " + Hsuit + " " + Tsuit;

        String[] Karten = new String[input.length()/3];
        //Fills the cards
        for(int i = 0;  i < input.length()/3; i++){
            String Karte = "" + input.charAt(3*i) + input.charAt((3*i)+1) + input.charAt((3*i) + 2);
            Karten[i] = Karte;
        }
        //System.out.println(Arrays.toString(Karten));

        for(int i = 0; i < Karten.length; i++){
            for(int j = 0; j < Karten.length; j++){
                if(i != j && Karten[i].equals(Karten[j])){
                    returnString = "GRESKA";
                }
            }
        }

        System.out.print(returnString);
        //System.out.println(Arrays.toString(Karten));
    }
}
