import java.io.BufferedReader;
import java.io.InputStreamReader;

/**
 * Created by August DH on 2017-07-04.
 */
public class simonSays3 {
    public static void main(String[]args){
        BufferedReader BR = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder builder = new StringBuilder();

        String test = "";
        String input = "";

        try{
            test = BR.readLine();
        }
        catch(Exception e){
        }

        int tests = Integer.parseInt(test);

        for(int i = 0; i < tests; i++){
            try{
                input = BR.readLine();
            }
            catch (Exception e){

            }

            String[] splitted = input.split(" ");
            if(splitted.length >= 2 && splitted[0].equals("simon") && splitted[1].equals("says")){
                for(int j = 2; j < splitted.length; j++){
                    builder.append(splitted[j]);
                    if (j!= splitted.length-1){
                        builder.append(" ");
                    }
                }
            }
            if(i != tests -1) {
                builder.append("\n");
            }
        }

        System.out.print(builder.toString());
    }
}
