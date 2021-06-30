import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Scanner;

/**
 * Created by August DH on 2016-12-10.
 */
public class Kemija {
    public static void main(String[]args){
        //Input
        String input;
        ArrayList<Character> inputList = new ArrayList<Character>();
        Scanner sc = new Scanner(System.in);
        input = sc.nextLine();

        for(int i = 0; i<input.length(); i++){
            inputList.add(input.charAt(i));
        }

       // System.out.println(inputList);

        int removeCount = 0;
        for(int i = 0; i < inputList.size(); i++){
        if(i < inputList.size()-2){
                if (((inputList.get(i) == 'a' && inputList.get(i+1) == 'p') || (inputList.get(i) == 'e' && inputList.get(i+1) == 'p') || (inputList.get(i) == 'i' && inputList.get(i+1) == 'p') || (inputList.get(i) == 'o' && inputList.get(i+1) == 'p') || (inputList.get(i) == 'u' && inputList.get(i+1) == 'p'))) {
                    inputList.remove(i + 1);
                    inputList.remove(i + 1);
               }
            }
        }

        //System.out.println(inputList);

        String returnString= "";
        for(int i = 0; i < inputList.size(); i++){
            returnString += inputList.get(i);
        }

        System.out.println(returnString);
    }
}
