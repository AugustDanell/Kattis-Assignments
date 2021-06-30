import java.util.Scanner;

/**
 * Created by August DH on 2017-06-27.
 */
public class Meheuric {
    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);
        String start = sc.nextLine();

        while(!start.equals("1 2 3 4 5")){
            char temp;
            boolean isSwapMade = false;

            if((int)start.charAt(0) > (int)start.charAt(2)){
                isSwapMade = true;
                char[] charArray = start.toCharArray();
                temp = charArray[0];
                charArray[0] = charArray[2];
                charArray[2] = temp;
                start = new String(charArray);
            }

            if(isSwapMade)
                System.out.println(start);

            isSwapMade = false;

            if((int)start.charAt(2) > (int)start.charAt(4)){
                isSwapMade = true;
                char[] charArray = start.toCharArray();
                temp = charArray[2];
                charArray[2] = charArray[4];
                charArray[4] = temp;
                start = new String(charArray);
            }

            if(isSwapMade)
                System.out.println(start);

            isSwapMade = false;

            if((int)start.charAt(4) > (int)start.charAt(6)){
                isSwapMade = true;
                char[] charArray = start.toCharArray();
                temp = charArray[4];
                charArray[4] = charArray[6];
                charArray[6] = temp;
                start = new String(charArray);
            }

            if(isSwapMade)
                System.out.println(start);

            isSwapMade = false;

            if((int)start.charAt(6) > (int)start.charAt(8)){
                isSwapMade = true;
                char[] charArray = start.toCharArray();
                temp = charArray[6];
                charArray[6] = charArray[8];
                charArray[8] = temp;
                start = new String(charArray);
            }

            if(isSwapMade)
            System.out.println(start);
        }
    }
}
