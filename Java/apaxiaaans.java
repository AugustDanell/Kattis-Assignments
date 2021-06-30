import java.util.ArrayList;
import java.util.Scanner;

/**
 * Created by August DH on 2016-12-11.
 */
public class apaxiaaans {
    public static void main(String[]args){
        //Input
        Scanner sc = new Scanner(System.in);
        String input = sc.nextLine();
        ArrayList<Character> inputlista = new ArrayList<Character>();

        //Fills a list with the given input
        for(int i = 0; i<input.length(); i++){
            inputlista.add(input.charAt(i));
        }

        //
        int i = 1;
        int removeCount = 0;

        while(i < (input.length()-removeCount)){
            if (inputlista.get(i) == inputlista.get(i - 1)) {
                inputlista.remove(i - 1);
                removeCount ++;
            }
            else {
                i++;
            }
        }
        //System.out.println(inputlista.get(0));

        String returnString = "";

        for(int j = 0; j<inputlista.size(); j++){
            returnString += inputlista.get(j);
        }

        System.out.println(returnString);
    }
}
