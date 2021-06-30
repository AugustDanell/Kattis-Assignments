import java.util.Scanner;

/**
 * Created by August DH on 2016-12-19.
 */
public class T9Spelling {
    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);
        int cases = sc.nextInt();
        sc.nextLine();
        StringBuilder builderBob = new StringBuilder();

        for(int i = 0; i < cases; i++){
            String message = sc.nextLine();

            builderBob.append("Case #" + (1+i) + ": ");

            for(int j = 0; j < message.length(); j++){
                if(message.charAt(j) == 'a'){
                    builderBob.append("2");
                    if(j!=(message.length()-1) && (message.charAt(j+1) == 'a' ||message.charAt(j+1) == 'b' || message.charAt(j+1) == 'c')){
                        builderBob.append(" ");
                    }
                }

                if(message.charAt(j) == 'b'){
                    builderBob.append("22");
                    if(j!=(message.length()-1) && (message.charAt(j+1) == 'a' ||message.charAt(j+1) == 'b' || message.charAt(j+1) == 'c')){
                        builderBob.append(" ");
                    }
                }

                if(message.charAt(j) == 'c'){
                    builderBob.append("222");
                    if(j!=(message.length()-1) && (message.charAt(j+1) == 'a' ||message.charAt(j+1) == 'b' || message.charAt(j+1) == 'c')){
                        builderBob.append(" ");
                    }
                }

                if(message.charAt(j) == 'd'){
                    builderBob.append("3");
                    if(j!=(message.length()-1) && (message.charAt(j+1) == 'd' ||message.charAt(j+1) == 'e' || message.charAt(j+1) == 'f')){
                        builderBob.append(" ");
                    }
                }

                if(message.charAt(j) == 'e'){
                    builderBob.append("33");
                    if(j!=(message.length()-1) && (message.charAt(j+1) == 'd' ||message.charAt(j+1) == 'e' || message.charAt(j+1) == 'f')){
                        builderBob.append(" ");
                    }
                }

                if(message.charAt(j) == 'f'){
                    builderBob.append("333");
                    if(j!=(message.length()-1) && (message.charAt(j+1) == 'd' ||message.charAt(j+1) == 'e' || message.charAt(j+1) == 'f')){
                        builderBob.append(" ");
                    }
                }

                if(message.charAt(j) == 'g'){
                    builderBob.append("4");
                    if(j!=(message.length()-1) && (message.charAt(j+1) == 'g' ||message.charAt(j+1) == 'h' || message.charAt(j+1) == 'i')){
                        builderBob.append(" ");
                    }
                }

                if(message.charAt(j) == 'h'){
                    builderBob.append("44");
                    if(j!=(message.length()-1) && (message.charAt(j+1) == 'g' ||message.charAt(j+1) == 'h' || message.charAt(j+1) == 'i')){
                        builderBob.append(" ");
                    }
                }

                if(message.charAt(j) == 'i'){
                    builderBob.append("444");
                    if(j!=(message.length()-1) && (message.charAt(j+1) == 'g' ||message.charAt(j+1) == 'h' || message.charAt(j+1) == 'i')){
                        builderBob.append(" ");
                    }
                }

                if(message.charAt(j) == 'j'){
                    builderBob.append("5");
                    if(j!=(message.length()-1) && (message.charAt(j+1) == 'j' ||message.charAt(j+1) == 'k' || message.charAt(j+1) == 'l')){
                        builderBob.append(" ");
                    }
                }

                if(message.charAt(j) == 'k'){
                    builderBob.append("55");
                    if(j!=(message.length()-1) && (message.charAt(j+1) == 'j' ||message.charAt(j+1) == 'k' || message.charAt(j+1) == 'l')){
                        builderBob.append(" ");
                    }
                }

                if(message.charAt(j) == 'l'){
                    builderBob.append("555");
                    if(j!=(message.length()-1) && (message.charAt(j+1) == 'j' ||message.charAt(j+1) == 'k' || message.charAt(j+1) == 'l')){
                        builderBob.append(" ");
                    }
                }

                if(message.charAt(j) == 'm'){
                    builderBob.append("6");
                    if(j!=(message.length()-1) && (message.charAt(j+1) == 'm' ||message.charAt(j+1) == 'n' || message.charAt(j+1) == 'o')){
                        builderBob.append(" ");
                    }
                }

                if(message.charAt(j) == 'n'){
                    builderBob.append("66");
                    if(j!=(message.length()-1) && (message.charAt(j+1) == 'm' ||message.charAt(j+1) == 'n' || message.charAt(j+1) == 'o')){
                        builderBob.append(" ");
                    }
                }

                if(message.charAt(j) == 'o'){
                    builderBob.append("666");
                    if(j!=(message.length()-1) && (message.charAt(j+1) == 'm' ||message.charAt(j+1) == 'n' || message.charAt(j+1) == 'o')){
                        builderBob.append(" ");
                    }
                }

                if(message.charAt(j) == 'p'){
                    builderBob.append("7");
                    if(j!=(message.length()-1) && (message.charAt(j+1) == 'p' ||message.charAt(j+1) == 'q' || message.charAt(j+1) == 'r' || message.charAt(j+1) == 's')){
                        builderBob.append(" ");
                    }
                }

                if(message.charAt(j) == 'q'){
                    builderBob.append("77");
                    if(j!=(message.length()-1) && (message.charAt(j+1) == 'p' ||message.charAt(j+1) == 'q' || message.charAt(j+1) == 'r' || message.charAt(j+1) == 's')){
                        builderBob.append(" ");
                    }
                }

                if(message.charAt(j) == 'r'){
                    builderBob.append("777");
                    if(j!=(message.length()-1) && (message.charAt(j+1) == 'p' ||message.charAt(j+1) == 'q' || message.charAt(j+1) == 'r' || message.charAt(j+1) == 's')){
                        builderBob.append(" ");
                    }
                }

                if(message.charAt(j) == 's'){
                    builderBob.append("7777");
                    if(j!=(message.length()-1) && (message.charAt(j+1) == 'p' ||message.charAt(j+1) == 'q' || message.charAt(j+1) == 'r' || message.charAt(j+1) == 's')){
                        builderBob.append(" ");
                    }
                }

                if(message.charAt(j) == 't'){
                    builderBob.append("8");
                    if(j!=(message.length()-1) && (message.charAt(j+1) == 't' ||message.charAt(j+1) == 'u' || message.charAt(j+1) == 'v' )){
                        builderBob.append(" ");
                    }
                }

                if(message.charAt(j) == 'u'){
                    builderBob.append("88");
                    if(j!=(message.length()-1) && (message.charAt(j+1) == 't' ||message.charAt(j+1) == 'u' || message.charAt(j+1) == 'v' )){
                        builderBob.append(" ");
                    }
                }

                if(message.charAt(j) == 'v'){
                    builderBob.append("888");
                    if(j!=(message.length()-1) && (message.charAt(j+1) == 't' ||message.charAt(j+1) == 'u' || message.charAt(j+1) == 'v' )){
                        builderBob.append(" ");
                    }
                }

                if(message.charAt(j) == 'w'){
                    builderBob.append("9");
                    if(j!=(message.length()-1) && (message.charAt(j+1) == 'w' ||message.charAt(j+1) == 'x' || message.charAt(j+1) == 'y' || message.charAt(j+1) == 'z' )){
                        builderBob.append(" ");
                    }
                }

                if(message.charAt(j) == 'x'){
                    builderBob.append("99");
                    if(j!=(message.length()-1) && (message.charAt(j+1) == 'w' ||message.charAt(j+1) == 'x' || message.charAt(j+1) == 'y' || message.charAt(j+1) == 'z' )){
                        builderBob.append(" ");
                    }
                }

                if(message.charAt(j) == 'y'){
                    builderBob.append("999");
                    if(j!=(message.length()-1) && (message.charAt(j+1) == 'w' ||message.charAt(j+1) == 'x' || message.charAt(j+1) == 'y' || message.charAt(j+1) == 'z' )){
                        builderBob.append(" ");
                    }
                }

                if(message.charAt(j) == 'z'){
                    builderBob.append("9999");
                    if(j!=(message.length()-1) && (message.charAt(j+1) == 'w' ||message.charAt(j+1) == 'x' || message.charAt(j+1) == 'y' || message.charAt(j+1) == 'z' )){
                        builderBob.append(" ");
                    }
                }

                if(message.charAt(j) == ' '){
                    builderBob.append("0");
                    if(j!=(message.length()-1) && (message.charAt(j+1) == ' ')){
                        builderBob.append(" ");
                    }
                }
            }
            builderBob.append("\n");
        }

        System.out.print(builderBob.toString());
    }
}
