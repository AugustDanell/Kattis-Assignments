import java.util.ArrayList;
import java.util.HashMap;
import java.util.Scanner;

/**
 * Created by August DH on 2017-03-04.
 */
public class hayPoints {
    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);
        StringBuilder builderBob = new StringBuilder();

        String input = sc.nextLine();
        String[] splitted = input.split(" ");

        int words = Integer.parseInt(splitted[0]);
        int people = Integer.parseInt(splitted[1]);

        HashMap<String, Integer> wordList = new HashMap<>();

        for(int i = 0; i < words; i++){
            String wordInput = sc.nextLine();
            splitted = wordInput.split(" ");

            String word = splitted[0];
            int points = Integer.parseInt(splitted[1]);

            wordList.put(word, points);
        }
        int periods = 0;
        int awardedPoints = 0;
        while(periods < people){
            String resume = sc.nextLine();
            if(resume.equals(".")){
                builderBob.append(awardedPoints + "\n");
                awardedPoints = 0;
                periods ++;
            }
            else{
                splitted = resume.split(" ");
                for(int i = 0; i < splitted.length; i++){
                    if(wordList.containsKey(splitted[i])){
                        awardedPoints += wordList.get(splitted[i]);
                    }
                }
            }
        }

        System.out.print(builderBob.toString());

    }
}
