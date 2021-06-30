import java.util.ArrayList;
import java.util.Scanner;

/**
 * Created by August DH on 2017-07-10.
 */
public class engineeringEnglish2 {
    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);
        ArrayList<String> usedWords = new ArrayList<>();
        StringBuilder builder = new StringBuilder();

        while(sc.hasNextLine()){
            String input = sc.nextLine();
            String[] splitted = input.split(" ");

            for(int i = 0; i < splitted.length; i++){
                boolean wordFound = false;
                for(int j = 0; j < usedWords.size(); j++){
                    if(splitted[i].equalsIgnoreCase(usedWords.get(j))){
                        wordFound = true;
                        break;
                    }
                }


                if(wordFound){
                    builder.append(".");
                }
                else{
                    builder.append(splitted[i]);
                    usedWords.add(splitted[i]);
                }

                if(i != splitted.length - 1){
                    builder.append(" ");
                }
            }
            builder.append("\n");
        }

        System.out.print(builder.toString());
    }
}
