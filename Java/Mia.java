import java.util.Scanner;

/**
 * Created by August DH on 2017-02-05.
 */
public class Mia {
    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);
        boolean run = true;
        StringBuilder builder = new StringBuilder();

        while(run){
            String input = sc.nextLine();
            int playerOneLevel = 0;
            int playerTwoLevel = 0;

            if(input.equals("0 0 0 0")){
                run = false;
            }
            //If the program is not terminated
            else{
                String[] splittedInput = input.split(" ");

                //Player One
                int S0 = Integer.parseInt(splittedInput[0]);
                int S1 = Integer.parseInt(splittedInput[1]);

                //Sets the level for player one
                if((S0 == 1 && S1 == 2 )||(S0 == 2 && S1 == 1)){
                    playerOneLevel = 3;
                }
                else if(S0 == S1){
                    playerOneLevel = 2;
                }
                else{
                    playerOneLevel = 1;
                }

                //Player Two
                int r0 = Integer.parseInt(splittedInput[2]);
                int r1 = Integer.parseInt(splittedInput[3]);

                //Sets the level for player two
                if((r0 == 1 && r1 == 2 )||(r0 == 2 && r1 == 1)){
                    playerTwoLevel = 3;
                }
                else if(r0 == r1){
                    playerTwoLevel = 2;
                }
                else{
                    playerTwoLevel = 1;
                }

                //System.out.println(playerOneLevel + " " + playerTwoLevel);//Test

                //Sets the victory conditions
                if(playerOneLevel > playerTwoLevel){
                    builder.append("Player 1 wins." + "\n");
                }
                else if(playerTwoLevel > playerOneLevel){
                    builder.append("Player 2 wins." + "\n");
                }

                //If the levels are the same
                if(playerOneLevel == playerTwoLevel){

                    //Case 1 - Tie no matter
                    if(playerOneLevel == 3){
                        builder.append("Tie." + "\n");
                    }

                    if(playerOneLevel == 2){
                        if(S0 > r0){
                            builder.append("Player 1 wins." + "\n");
                        }
                        else if(S0 == r0){
                            builder.append("Tie." + "\n");
                        }
                        else{
                            builder.append("Player 2 wins." + "\n");
                        }
                    }

                    //Case 3 - Not the same
                    if(playerOneLevel == 1){
                        int playerOneSum = 0;
                        int playerTwoSum = 0;
                        //Creating the player sums
                        //Player one
                        if(S0>S1){
                            playerOneSum = (S0*10) + S1;
                        }
                        else{
                            playerOneSum = (S1*10) + S0;
                        }
                        //Player two
                        if(r0 > r1){
                            playerTwoSum = (r0 * 10) + r1;
                        }
                        else{
                            playerTwoSum = (r1 * 10) + r0;
                        }

                        // Funkar - System.out.println(playerOneSum + " " + playerTwoSum);
                        //The victory conditions for case 3
                        if(playerOneSum > playerTwoSum){
                            builder.append("Player 1 wins." + "\n");
                        }
                        else if(playerTwoSum > playerOneSum){
                            builder.append("Player 2 wins." + "\n");
                        }
                        else if(playerOneSum == playerTwoSum){
                            builder.append("Tie." + "\n");
                        }


                    }
                }

            }
        }
        System.out.print(builder.toString());
    }
}
