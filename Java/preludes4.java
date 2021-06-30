import java.util.Scanner;

/**
 * Created by August DH on 2017-08-27.
 */
public class preludes4 {
    public static String getNote(String input){

        if(input.equals("A#")){
            return "Bb";
        }
        else if(input.equals("C#")){
            return "Db";
        }
        else if(input.equals("D#")){
            return "Eb";
        }
        else if(input.equals("F#")){
            return "Gb";
        }
        else if(input.equals("G#")){
            return "Ab";
        }
        else if(input.equals("Bb")){
            return "A#";
        }
        else if(input.equals("Db")){
            return "C#";
        }
        else if(input.equals("Eb")){
            return "D#";
        }
        else if(input.equals("Gb")){
            return "F#";
        }
        else if(input.equals("Ab")){
            return "G#";
        }

        return "UNIQUE";
    }

    public static void print(int currentCase, String input){
        String[] splitted = input.split(" ");
        String appendage = "";
        if(!getNote(splitted[0]).equals("UNIQUE")){
            appendage = " " + splitted[1];
        }

        System.out.println("Case " + currentCase + ": " + getNote(splitted[0]) + appendage);
    }

    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);
        int currentCase = 1;

        while(sc.hasNextLine()){
            String input = sc.nextLine();
            print(currentCase, input);
            currentCase ++;
        }
    }
}
