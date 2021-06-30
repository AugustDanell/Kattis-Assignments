import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

/**
 * Created by August DH on 2016-12-31.
 */
public class RaggedRight {
    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);
        String input = sc.nextLine();
        //ArrayList<String> Lines = new ArrayList<>();
        ArrayList<Integer> LineLengths = new ArrayList<>();
        int i = 0;
        int sum = 0;
        while(sc.hasNextLine()){
            if(i!= 0){
                input = sc.nextLine();
            }

           // Lines.add(input);
            LineLengths.add(input.length());
        i++;
        }

        if(LineLengths.size() != 0 && LineLengths.size() != 1) {
            int sumOfLongestSentence = LineLengths.get(0);
            for (int j = 0; j < LineLengths.size() - 1; j++) {
                if (LineLengths.get(j + 1) > sumOfLongestSentence) {
                    sumOfLongestSentence = LineLengths.get(j + 1);
                }
            }

            LineLengths.remove(LineLengths.size() - 1);

            for (int j = 0; j < LineLengths.size(); j++) {
                if (sumOfLongestSentence - LineLengths.get(j) != 0) {
                    sum += Math.pow((sumOfLongestSentence - LineLengths.get(j)), 2);
                }
            }
        }
        else{
            sum = 0;
        }
        System.out.print(sum);
    }
}
