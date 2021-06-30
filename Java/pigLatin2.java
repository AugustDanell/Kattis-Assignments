import java.util.Scanner;

/**
 * Created by August DH on 2017-08-13.
 */
public class pigLatin2 {
    public static boolean testVowel(char first){
        if(first == 'a' || first == 'e' || first == 'i' || first == 'o' || first == 'u' || first == 'y'){
            //Test for vowels
            return true;
        }
        else{
            return false;
        }
    }

    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);
        StringBuilder builder = new StringBuilder();

        while(sc.hasNextLine()){
            String input = sc.nextLine();
            String[] splittedInput = input.split(" ");

            for(int i = 0; i < splittedInput.length; i++){
                char first = splittedInput[i].charAt(0);
                if(testVowel(first)){
                    builder.append(splittedInput[i] + "yay");
                }
                else{
                    String concat = "" + first;
                    splittedInput[i] = splittedInput[i].substring(1);
                    while(splittedInput[i].length() > 0 && !testVowel(splittedInput[i].charAt(0))){
                        concat += "" + splittedInput[i].charAt(0);
                        splittedInput[i] = splittedInput[i].substring(1);
                    }

                    builder.append(splittedInput[i] + concat + "ay");
                }

                if(i != splittedInput.length - 1){
                    //Append space to all but the last element
                    builder.append(" ");
                }
            }

            builder.append("\n");
        }

        System.out.print(builder.toString());
    }
}
