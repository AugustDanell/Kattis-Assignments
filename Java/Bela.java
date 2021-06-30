import java.util.Scanner;

/**
 * Created by August DH on 2016-12-11.
 */
public class Bela {
    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);
        StringBuilder BuilderBob = new StringBuilder();

        String input = sc.nextLine();
        String[] splittedInput = input.split(" ");

        int numberOfHands = Integer.parseInt(splittedInput[0]);
        String dominantSuit = splittedInput[1];

        int totalPoints = 0;
        for(int i = 0; i < 4*numberOfHands; i++){
            String Card = sc.nextLine();
            if(Card.charAt(1) == dominantSuit.charAt(0)){

                if(Card.charAt(0) == 'A'){
                    totalPoints += 11;
                }

                if(Card.charAt(0) == 'K'){
                    totalPoints += 4;
                }

                if(Card.charAt(0) == 'Q'){
                    totalPoints += 3;
                }

                if(Card.charAt(0) == 'J'){
                    totalPoints += 20;
                }

                if(Card.charAt(0) == 'T'){
                    totalPoints += 10;
                }

                if(Card.charAt(0) == '9'){
                    totalPoints += 14;
                }
                if(Card.charAt(0) == '8'){
                    totalPoints += 0;
                }

                if(Card.charAt(0) == '7'){
                    totalPoints += 0;
                }
            }

            else{
                if(Card.charAt(0) == 'A'){
                    totalPoints += 11;
                }

                if(Card.charAt(0) == 'K'){
                    totalPoints += 4;
                }

                if(Card.charAt(0) == 'Q'){
                    totalPoints += 3;
                }

                if(Card.charAt(0) == 'J'){
                    totalPoints += 2;
                }

                if(Card.charAt(0) == 'T'){
                    totalPoints += 10;
                }

                if(Card.charAt(0) == '9'){
                    totalPoints += 0;
                }

                if(Card.charAt(0) == '8'){
                    totalPoints += 0;
                }

                if(Card.charAt(0) == '7'){
                    totalPoints += 0;
                }
            }
        }
        System.out.print(totalPoints);
    }
}
