import java.util.Scanner;

/**
 * Created by August DH on 2017-02-21.
 */
public class PrintingCosts {
    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);
        StringBuilder builder = new StringBuilder();

        while(sc.hasNextLine()){
            int cost = 0;
            String input = sc.nextLine();
            for(int i = 0; i < input.length(); i++){
                char a = input.charAt(i);

                if(a == '&'){
                    cost += 24;
                }
                else if(a == ','){
                    cost += 7;
                }
                else if(a == '2'){
                    cost += 22;
                }
                else if(a == '8'){
                    cost += 23;
                }
                else if(a == '>'){
                    cost += 10;
                }
                else if( a == 'D'){
                    cost += 26;
                }
                else if(a == 'J'){
                    cost += 18;
                }
                else if(a == 'P'){
                    cost += 23;
                }
                else if(a == 'V'){
                    cost += 19;
                }
                else if(a == '\\'){
                    cost += 10;
                }
                else if(a == 'b'){
                    cost += 25;
                }
                else if(a == 'h'){
                    cost += 21;
                }
                else if(a == 'n'){
                    cost += 18;
                }
                else if(a == 't'){
                    cost += 17;
                }
                else if(a == 'z'){
                    cost += 19;
                }

                else if(a == '!'){
                    cost += 9;
                }

                else if(a == '\''){
                    cost += 3;
                }
                else if(a == '-'){
                    cost += 7;
                }
                else if(a == '3'){
                    cost += 23;
                }
                else if(a == '9'){
                    cost += 26;
                }
                else if(a == '?'){
                    cost += 15;
                }
                else if(a == 'E'){
                    cost += 26;
                }
                else if(a == 'K'){
                    cost += 21;
                }
                else if(a == 'Q'){
                    cost += 31;
                }
                else if(a == 'W'){
                    cost += 26;
                }
                else if(a == ']'){
                    cost += 18;
                }
                else if(a == 'c'){
                    cost += 17;
                }
                else if(a == 'i'){
                    cost += 15;
                }
                else if(a == 'o'){
                    cost += 20;
                }
                else if(a == 'u'){
                    cost += 17;
                }
                else if(a == '{'){
                    cost += 18;
                }
                else if(a == '\"'){
                    cost += 6;
                }
                else if(a == '('){
                    cost += 12;
                }
                else if(a == '.'){
                    cost += 4;
                }
                else if(a == ':'){
                    cost += 8;
                }
                else if(a == '@'){
                    cost += 32;
                }
                else if(a == 'F'){
                    cost += 20;
                }
                else if(a == 'L'){
                    cost += 16;
                }
                else if(a == 'R'){
                    cost += 28;
                }
                else if(a == 'X'){
                    cost += 18;
                }
                else if(a == '^'){
                    cost += 7;
                }
                else if(a == 'd'){
                    cost += 25;
                }
                else if(a == 'j'){
                    cost += 20;
                }
                else if (a == 'p'){
                    cost += 25;
                }
                else if (a == 'v'){
                    cost += 13;
                }
                else if (a == '|'){
                    cost += 12;
                }
                else if (a == '#'){
                    cost += 24;
                }
                else if (a == ')'){
                    cost += 12;
                }
                else if(a == '/'){
                    cost += 10;
                }
                else if(a == '5'){
                    cost += 27;
                }
                else if(a == ';'){
                    cost += 11;
                }
                else if(a == 'A'){
                    cost += 24;
                }
                else if(a == 'G'){
                    cost += 25;
                }
                else if(a == 'M'){
                    cost += 28;
                }
                else if(a == 'S'){
                    cost += 25;
                }
                else if(a == 'Y'){
                    cost += 14;
                }
                else if(a=='_'){
                    cost += 8;
                }
                else if(a == 'e'){
                    cost += 23;
                }
                else if(a == 'k'){
                    cost += 21;
                }
                else if(a == 'q'){
                    cost += 25;
                }
                else if(a == 'w'){
                    cost += 19;
                }
                else if(a == '}'){
                    cost += 18;
                }
                else if(a == '$'){
                    cost += 29;
                }
                else if(a == '*'){
                    cost += 17;
                }
                else if(a == '0'){
                    cost += 22;
                }
                else if(a == '6'){
                    cost += 26;
                }
                else if(a == '<'){
                    cost += 10;
                }
                else if(a == 'B'){
                    cost += 29;
                }
                else if(a == 'H'){
                    cost += 25;
                }
                else if(a == 'N'){
                    cost += 25;
                }
                else if(a == 'T'){
                    cost += 16;
                }
                else if(a == 'Z'){
                    cost += 22;
                }
                else if(a == '`'){
                    cost += 3;
                }
                else if(a== 'f'){
                    cost += 18;
                }
                else if(a == 'l'){
                    cost += 16;
                }
                else if(a == 'r'){
                    cost += 13;
                }
                else if(a == 'x'){
                    cost += 13;
                }
                else if(a == '~'){
                    cost += 9;
                }
                else if(a=='%'){
                    cost += 22;
                }
                else if(a == '+'){
                    cost += 13;
                }
                else if(a == '1'){
                    cost += 19;
                }
                else if(a == '7'){
                    cost += 16;
                }
                else if(a == '='){
                    cost += 14;
                }
                else if(a == 'C'){
                    cost += 20;
                }
                else if(a == 'I'){
                    cost += 18;
                }
                else if(a == 'O'){
                    cost += 26;
                }
                else if(a == 'U'){
                    cost += 23;
                }
                else if(a == '['){
                    cost += 18;
                }
                else if(a == 'a'){
                    cost += 23;
                }
                else if(a == 'g'){
                    cost += 30;
                }
                else if(a == 'm'){
                    cost += 22;
                }
                else if(a == 's'){
                    cost += 21;
                }
                else if(a == 'y'){
                    cost += 24;
                }
                else if(a == '4'){
                    cost += 21;
                }
            }
            builder.append(cost + "\n");
        }
    System.out.print(builder.toString());
    }

}
