import java.util.HashMap;
import java.util.Scanner;

/**
 * Created by August DH on 2017-08-01.
 */
public class variableArithmetic {
    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);
        StringBuilder builder = new StringBuilder();

        boolean run = true;
        HashMap<String, Integer> variableList = new HashMap<>();
        while (run){
            String input = sc.nextLine();
            if(input.equals("0")){
                run = false;
            }else{
                int sum = 0;
                String helpString = "";
                String[] splitted = input.split(" ");

                //If it is a variable assignment:
                if(splitted.length > 1 && splitted[1].equals("=")){
                    variableList.put(splitted[0], Integer.parseInt(splitted[2]));
                }
                else{
                    for(int i = 0; i < splitted.length; i++){
                        try{
                            sum += Integer.parseInt(splitted[i]);
                        }
                        catch (NumberFormatException e){
                            //If not an integer, but a string.

                            //Check if the value is stored.
                            if(variableList.containsKey(splitted[i])){
                                sum += variableList.get(splitted[i]);
                            }
                            else{
                                if(!splitted[i].equals("+"))
                                    helpString += " + " + splitted[i];
                            }
                        }
                    }

                    if(sum != 0) {
                        builder.append(sum + helpString + "\n");
                    }
                    else{
                        //Sum = 0.  -   omit Sum.
                        builder.append(helpString.substring(3) + "\n");
                    }
                }
            }
        }

        System.out.print(builder.toString());
    }
}
