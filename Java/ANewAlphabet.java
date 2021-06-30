import java.util.Scanner;

/**
 * Created by August DH on 2016-12-16.
 */
public class ANewAlphabet {
    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);
        StringBuilder BuilderBob = new StringBuilder();

        String input = sc.nextLine();
        for(int i = 0; i < input.length(); i++){
            if(input.charAt(i) == 'a' || input.charAt(i) == 'A'){
                BuilderBob.append("@");
            }

            else if(input.charAt(i) == 'b' || input.charAt(i) == 'B'){
                BuilderBob.append("8");
            }

            else if(input.charAt(i) == 'c' || input.charAt(i) == 'C'){
                BuilderBob.append("(");
            }

            else if(input.charAt(i) == 'd' || input.charAt(i) == 'D'){
                BuilderBob.append("|)");
            }

            else if(input.charAt(i) == 'e' || input.charAt(i) == 'E'){
                BuilderBob.append("3");
            }

            else if(input.charAt(i) == 'f' || input.charAt(i) == 'F'){
                BuilderBob.append("#");
            }

            else if(input.charAt(i) == 'g' || input.charAt(i) == 'G'){
                BuilderBob.append("6");
            }

            else if(input.charAt(i) == 'h' || input.charAt(i) == 'H'){
                BuilderBob.append("[-]");
            }

            else if(input.charAt(i) == 'i' || input.charAt(i) == 'I'){
                BuilderBob.append("|");
            }

            else if(input.charAt(i) == 'j' || input.charAt(i) == 'J'){
                BuilderBob.append("_|");
            }

            else if(input.charAt(i) == 'k' || input.charAt(i) == 'K'){
                BuilderBob.append("|<");
            }

            else if(input.charAt(i) == 'l' || input.charAt(i) == 'L'){
                BuilderBob.append("1");
            }

            else if(input.charAt(i) == 'm' || input.charAt(i) == 'M'){
                BuilderBob.append("[]\\/[]");
            }

            else if(input.charAt(i) == 'n' || input.charAt(i) == 'N'){
                BuilderBob.append("[]\\[]");
            }

            else if(input.charAt(i) == 'o' || input.charAt(i) == 'O'){
                BuilderBob.append("0");
            }

            else if(input.charAt(i) == 'p' || input.charAt(i) == 'P'){
                BuilderBob.append("|D");
            }

            else if(input.charAt(i) == 'q' || input.charAt(i) == 'Q'){
                BuilderBob.append("(,)");
            }

            else if(input.charAt(i) == 'r' || input.charAt(i) == 'R'){
                BuilderBob.append("|Z");
            }

            else if(input.charAt(i) == 's' || input.charAt(i) == 'S'){
                BuilderBob.append("$");
            }

            else if(input.charAt(i) == 't' || input.charAt(i) == 'T'){
                BuilderBob.append("']['");
            }

            else if(input.charAt(i) == 'u' || input.charAt(i) == 'U'){
                BuilderBob.append("|_|");
            }

            else if(input.charAt(i) == 'v' || input.charAt(i) == 'V'){
                BuilderBob.append("\\/");
            }

            else if(input.charAt(i) == 'w' || input.charAt(i) == 'W'){
                BuilderBob.append("\\/\\/");
            }

            else if(input.charAt(i) == 'x' || input.charAt(i) == 'X'){
                BuilderBob.append("}{");
            }

            else if(input.charAt(i) == 'y' || input.charAt(i) == 'Y'){
                BuilderBob.append("`/");
            }

            else if(input.charAt(i) == 'z' || input.charAt(i) == 'Z'){
                BuilderBob.append("2");
            }
            else{
                BuilderBob.append(input.charAt(i));
            }
        }

        System.out.print(BuilderBob.toString());
    }
}
