import java.util.Arrays;
import java.util.Scanner;

/**
 * Created by August DH on 2016-12-10.
 */
public class ReverseRot {
    public static void main(String[]args){
        int rotatoes = 0;
        int stringCount = 0;
        int returnCount = 0;

        boolean[] dangerZone = new boolean[50];

        String processedString = "";
        String swappedString = "";
        String rotatedString = "";
        String returnString[] = new String[50];
        String input = "1";
        StringBuilder builderBob = new StringBuilder();
        boolean iterated = false;

        Scanner sc = new Scanner(System.in);
        while(Integer.parseInt(input.substring(0,1)) != 0) {
            /*returnCount ++;
            returnString = new String[returnCount];*/

            input = sc.nextLine();
            //System.out.println(Integer.parseInt(input.substring(0,1)));

            //String process and optaining the rotatoes
            if(input.length() > 1) {
                if (input.charAt(1) >= '0' && input.charAt(1) <= '9') {
                    rotatoes = Integer.parseInt(input.substring(0, 2));
                    processedString = input.substring(3, input.length());
                } else {
                    rotatoes = Integer.parseInt(input.substring(0, 1));
                    processedString = input.substring(2, input.length());
                }

                //String swapping
                char[] c = processedString.toCharArray();
                for (int i = 0; i < processedString.length() / 2; i++) {


                    //Swapping the string characters
                    char temp = c[i];
                    c[i] = c[c.length - 1 - i];
                    c[c.length - 1 - i] = temp;

                }
                swappedString = new String(c);
                //System.out.println(swappedString);

                //Time for some rotatoes
                int[] asciiChart = new int[swappedString.length()];


                for (int i = 0; i < swappedString.length(); i++) {
                    dangerZone[i] = false;
                    int helpRest;
                    asciiChart[i] = ((int) (swappedString.charAt(i)) + rotatoes);
                    boolean addedTo95 = false;

                    if((int)swappedString.charAt(i) == 95 && asciiChart[i] > 96){
                        asciiChart[i] = 91 + (rotatoes);
                        addedTo95 = true;
                    }

                    if(asciiChart[i]>90 || asciiChart[i] == 46+rotatoes){
                        dangerZone[i] = true;
                    }

                    if (asciiChart[i] == 92 || (asciiChart[i] == 96 && (int) swappedString.charAt(i) == 95 )) {
                        asciiChart[i] = 46;
                        //dangerZone[i] = true;
                    }

                    else if(asciiChart[i] > 46  && dangerZone[i] && asciiChart[i] != 91){
                        asciiChart[i] = (asciiChart[i] % 46) + 64;
                    }
                    //System.out.println(asciiChart[i]);
                    while (asciiChart[i] > 92 && dangerZone[i] && asciiChart[i] != 95){
                        asciiChart[i] = (asciiChart[i] % 92) + 64;
                    }

                    if (asciiChart[i] == 91 && !addedTo95) {
                        asciiChart[i] = 95;
                    }

                }

                for (int i = 0; i < swappedString.length(); i++) {
                    returnString[stringCount] += ((char) asciiChart[i]);
                    // System.out.println(returnString);
                }

            stringCount ++;
            }
        }
        for(int i = 0; i < stringCount; i++) {
            System.out.println(returnString[i].substring(4,returnString[i].length()));
           // if(returnString[i+1] != null){
           //     System.out.println();
           // }
        }

    }
}
