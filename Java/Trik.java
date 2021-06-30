import java.util.Scanner;

/**
 * Created by August DH on 2016-12-09.
 */
public class Trik {
    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);
        String Moves;
        int ballPos = 1;
        boolean Pass = false;

        Moves = sc.nextLine();
        //System.out.println(Moves.charAt(0));  ((int) (swappedString.charAt(i)) + rotatoes);
        for(int i = 0; i < Moves.length(); i++){
            Pass = false;

            //System.out.println(Moves + ballPos + (int)(Moves.charAt(i)));
            if(Moves.charAt(i) == 'A' && ballPos == 1 && Pass == false){
                ballPos = 2;
                Pass = true;
            }
            if(Moves.charAt(i) == 'A' && ballPos == 2 && Pass == false){
                ballPos = 1;
                Pass = true;
            }

            if(Moves.charAt(i) == 'B' && ballPos == 2 && Pass == false){
                ballPos = 3;
                Pass = true;
            }
            if(Moves.charAt(i) == 'B' && ballPos == 3 && Pass == false){
                ballPos = 2;
                Pass = true;
            }

            if(Moves.charAt(i) == 'C' && ballPos == 1 && Pass == false){
                ballPos = 3;
                Pass = true;
            }
            if(Moves.charAt(i) == 'C' && ballPos == 3 && Pass == false){
                ballPos = 1;
                Pass = true;
            }

        }
        System.out.println(ballPos);
    }
}
