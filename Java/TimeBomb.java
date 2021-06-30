import java.util.Scanner;

/**
 * Created by August DH on 2016-12-17.
 */
public class TimeBomb {
    public static void main (String[]args){
        Scanner sc = new Scanner(System.in);
        String[] savedLines = new String[5];
        String input = "";
        boolean boom = false;

        for(int i = 0; i < 5; i++){
            input = sc.nextLine();
            savedLines[i] = input;
            //System.out.println(input.length());

        }
        int numbers = (input.length()+1)/4;
        String[] savedNumbers = new String[numbers];

        for(int i = 0; i < numbers; i++){
            savedNumbers[i] = savedLines[0].substring((4*i),((4*i))+3)
                            + " " + savedLines[1].substring((4*i),((4*i))+3)
                            + " " + savedLines[2].substring((4*i),((4*i))+3)
                            + " " + savedLines[3].substring((4*i),((4*i))+3)
                            + " " + savedLines[4].substring((4*i),((4*i))+3);
        }

        int[] integerizedNumbers = new int[numbers];
        for(int i = 0; i < numbers; i++){
            //System.out.println(savedNumbers[i]);
            boolean couldNotRead = true;
            if(savedNumbers[i].equals("*** * * * * * * ***")){
                integerizedNumbers[i] = 0;
                couldNotRead = false;
            }

            if(savedNumbers[i].equals("  *   *   *   *   *")){
                integerizedNumbers[i] = 1;
                couldNotRead = false;
            }

            if(savedNumbers[i].equals("***   * *** *   ***")){
                integerizedNumbers[i] = 2;
                couldNotRead = false;
            }

            if(savedNumbers[i].equals("***   * ***   * ***")){
                integerizedNumbers[i] = 3;
                couldNotRead = false;
            }

            if(savedNumbers[i].equals("* * * * ***   *   *")){
                integerizedNumbers[i] = 4;
                couldNotRead = false;
            }

            if(savedNumbers[i].equals("*** *   ***   * ***")){
                integerizedNumbers[i] = 5;
                couldNotRead = false;
            }

            if(savedNumbers[i].equals("*** *   *** * * ***")){
                integerizedNumbers[i] = 6;
                couldNotRead = false;
            }

            if(savedNumbers[i].equals("***   *   *   *   *")){
                integerizedNumbers[i] = 7;
                couldNotRead = false;
            }

            if(savedNumbers[i].equals("*** * * *** * * ***")){
                integerizedNumbers[i] = 8;
                couldNotRead = false;
            }

            if(savedNumbers[i].equals("*** * * ***   * ***")){
                integerizedNumbers[i] = 9;
                couldNotRead = false;
            }

            if(couldNotRead){
                boom = true;
            }
        }

        String returnString = "";
        for(int i = 0; i < integerizedNumbers.length; i++){
            returnString += integerizedNumbers[i];
            //System.out.print("Test");
        }

        //System.out.print(returnString);
        int returnInt = Integer.parseInt(returnString);
        if(!boom) {
            if (returnInt%6 == 0) {
                boom = false;
            }

            if(returnInt% 6 != 0){
                boom = true;
            }
        }

        if(!boom) {
            System.out.print("BEER!!");
        }
        else{
            System.out.print("BOOM!!");
        }
    }
}
