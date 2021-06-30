import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Scanner;
import java.io.BufferedReader;

/**
 * Created by August DH on 2017-02-18.
 */
public class Babelfish {
    public static void main(String[]args){
        BufferedReader BR = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder builder = new StringBuilder();

        HashMap<String, String> wordMap = new HashMap<>();
        boolean isTranslation = true;
        String input = " ";


        //Testing with Buffered Reader and HashMap instead of a scanner.
        try {
            while (isTranslation) {
                input = BR.readLine();

                if (input.length() == 0) {
                    isTranslation = false;
                    //Once this statement is reached the loop will terminate.
                }

                if (isTranslation) {
                    String[] split = input.split(" ");
                    wordMap.put(split[1], split[0]); //The translation to the word.
                }

            }

            //Similar to Sc.hasNextLine() - But for the Buffered reader.
            while(((input = BR.readLine())) != null){

                if(wordMap.containsKey(input)){
                    builder.append(wordMap.get(input) + "\n");  //If word found - appended as before to the stringBuilder
                }
                else{
                    builder.append("eh\n");                     //If not - append "eh".
                }
            }
        }

        catch (Exception e){
            //Not sure from the examples and documentation what to have in here the exception.
        }

        System.out.print(builder.toString()); //Print
    }
}
