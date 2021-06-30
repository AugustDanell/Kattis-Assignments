import java.util.HashMap;
import java.util.Scanner;

public class addingWords {
    public static HashMap<String, Integer> variables = new HashMap<>();

    public static String calc(String inp){
        String[] split = inp.split(" ");
        String conc = inp.substring(5, inp.length());
        int sum = 0;

        if(variables.containsKey(split[1])) {
            sum = variables.get(split[1]); //Get the first value
        }
        else{
            return conc + " unknown";
        }

        for(int i = 2; i < split.length -1; i++){
            int coff = 1;
            if(split[i].equals("-")){
                coff = -1;
            }
            i++; // Now we roll over after change of coff.

            //Check validity of variable.
            if(variables.containsKey(split[i])){
                sum += coff * variables.get(split[i]);
            }
            else{
                return conc + " unknown";
            }
        }
        // Here we should have a valid sum.
        String answer = findVar(sum);
        if(answer.equals("UN-FUCKING-VALID")){
            return conc + " unknown";
        }

        // Like an else statement.
        return conc + " " + answer;
    }

    public static String findVar(int sum){
        for(String key : variables.keySet()){
            if(variables.get(key) == sum){
                return key;
            }
        }
        return "UN-FUCKING-VALID";
    }

    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);

        while(sc.hasNextLine()){
            String input = sc.nextLine();
            if(input.substring(0, 3).equals("def")){
                // Defining variables

                String[] split = input.split(" ");
                variables.put(split[1], Integer.parseInt(split[2]));    // Adds the variable.
            }
            else if(input.substring(0, 4).equals("calc")){
                // Here we make calculations and print them.

                System.out.println(calc(input));
            }
            else{
                // If previous cases fail, the wanted command must be clear.
                // Here we clear out all previous values by redefining variables.

                variables = new HashMap<>();    // Reset
            }
        }
    }
}
