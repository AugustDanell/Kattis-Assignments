import java.util.Scanner;

/**
 * Created by August DH on 2017-03-09.
 */
public class quickBrownFox2 {
    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);
        StringBuilder builder = new StringBuilder();

        int cases = sc.nextInt();
        sc.nextLine();

        for(int i = 0; i < cases; i++){
            String input = sc.nextLine();
            String missingLetters = "";

            if(!input.contains("a") && !input.contains("A")){
                missingLetters += "a";
            }
            if(!input.contains("b") && !input.contains("B")){
                missingLetters += "b";
            }
            if(!input.contains("c") && !input.contains("C")){
                missingLetters += "c";
            }
            if(!input.contains("d") && !input.contains("D")){
                missingLetters += "d";
            }
            if(!input.contains("e") && !input.contains("E")){
                missingLetters += "e";
            }
            if(!input.contains("f") && !input.contains("F")){
                missingLetters += "f";
            }
            if(!input.contains("g") && !input.contains("G")){
                missingLetters += "g";
            }
            if(!input.contains("h") && !input.contains("H")){
                missingLetters += "h";
            }
            if(!input.contains("i") && !input.contains("I")){
                missingLetters += "i";
            }
            if(!input.contains("j") && !input.contains("J")){
                missingLetters += "j";
            }
            if(!input.contains("k") && !input.contains("K")){
                missingLetters += "k";
            }
            if(!input.contains("l") && !input.contains("L")){
                missingLetters += "l";
            }
            if(!input.contains("m") && !input.contains("M")){
                missingLetters += "m";
            }
            if(!input.contains("n") && !input.contains("N")){
                missingLetters += "n";
            }
            if(!input.contains("o") && !input.contains("O")){
                missingLetters += "o";
            }
            if(!input.contains("p") && !input.contains("P")){
                missingLetters += "p";
            }
            if(!input.contains("q") && !input.contains("Q")){
                missingLetters += "q";
            }
            if(!input.contains("r") && !input.contains("R")){
                missingLetters += "r";
            }
            if(!input.contains("s") && !input.contains("S")){
                missingLetters += "s";
            }
            if(!input.contains("t") && !input.contains("T")){
                missingLetters += "t";
            }
            if(!input.contains("u") && !input.contains("U")){
                missingLetters += "u";
            }
            if(!input.contains("v") && !input.contains("V")){
                missingLetters += "v";
            }
            if(!input.contains("w") && !input.contains("W")){
                missingLetters += "w";
            }
            if(!input.contains("x") && !input.contains("X")){
                missingLetters += "x";
            }
            if(!input.contains("y") && !input.contains("Y")){
                missingLetters += "y";
            }
            if(!input.contains("z") && !input.contains("Z")){
                missingLetters += "z";
            }

            if(missingLetters.equals("")){
                builder.append("pangram\n");
            }
            else{
                builder.append("missing " + missingLetters + "\n");
            }
        }

        System.out.print(builder.toString());
    }
}
