import java.util.Scanner;

/**
 * Created by August DH on 2016-12-19.
 */
public class EraseSecurely {
    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);
        String input = sc.nextLine();
        String[] splittedInput = input.split(" ");
        int securityLevel = Integer.parseInt(splittedInput[0]);
        boolean invert = false;
        String startString = "";
        String endString = "";

        for(int i = 0; i < 2; i++){
            String binInput = sc.nextLine();

            if(i == 0){
                startString = binInput;
            }
            if(i == 1){
                endString = binInput;
            }
        }

        //System.out.print(startString + "\n" + endString + "\n" + "\n");

        /*

        Attempting to make an int conjures a number format exception.
        long startInt = Long.parseLong(startString);
        long endInt = Long.parseLong(endString);
*/
        if(securityLevel % 2 == 1){
            invert = true;
        }
        //long permutedInt = startInt;
        String permutedString = "";
        if(invert){
            //permutedInt = ~startInt;
            for(int i = 0; i < startString.length(); i++){
                if(startString.charAt(i) == '1'){
                    permutedString += "0";
                }
                else{
                    permutedString += "1";
                }
            }
        }
        else{
            permutedString = startString;
        }

        if(permutedString.equals(endString)){
            System.out.print("Deletion succeeded");
        }
        else{
            System.out.print("Deletion failed");
        }
    }
}
