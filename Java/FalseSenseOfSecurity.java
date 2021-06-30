import java.util.Scanner;

/**
 * Created by August DH on 2017-02-14.
 */
public class FalseSenseOfSecurity {
    public static String morsify(String input){
        String morse = "";
        String numberKey = "";

        for(int i = 0; i < input.length(); i++){
            if(input.charAt(i) == 'A'){
                morse += ".-";
                numberKey += "2";
            }
            else if(input.charAt(i) == 'B'){
                morse += "-...";
                numberKey += "4";
            }
            else if(input.charAt(i) == 'C'){
                morse += "-.-.";
                numberKey += "4";
            }
            else if(input.charAt(i) == 'D'){
                morse += "-..";
                numberKey += "3";
            }
            else if(input.charAt(i) == 'E'){
                morse += ".";
                numberKey += "1";
            }
            else if(input.charAt(i) == 'F'){
                morse += "..-.";
                numberKey += "4";
            }
            else if(input.charAt(i) == 'G'){
                morse += "--.";
                numberKey += "3";
            }
            else if(input.charAt(i) == 'H'){
                morse += "....";
                numberKey += "4";
            }
            else if(input.charAt(i) == 'I'){
                morse += "..";
                numberKey += "2";
            }
            else if(input.charAt(i) == 'J'){
                morse += ".---";
                numberKey += "4";
            }
            else if(input.charAt(i) == 'K'){
                morse += "-.-";
                numberKey += "3";
            }
            else if(input.charAt(i) == 'L'){
                morse += ".-..";
                numberKey += "4";
            }
            else if(input.charAt(i) == 'M'){
                morse += "--";
                numberKey += "2";
            }
            else if(input.charAt(i) == 'N'){
                morse += "-.";
                numberKey += "2";
            }
            else if(input.charAt(i) == 'O'){
                morse += "---";
                numberKey += "3";
            }
            else if(input.charAt(i) == 'P'){
                morse += ".--.";
                numberKey += "4";
            }
            else if(input.charAt(i) == 'Q'){
                morse += "--.-";
                numberKey += "4";
            }
            else if(input.charAt(i) == 'R'){
                morse += ".-.";
                numberKey += "3";
            }
            else if(input.charAt(i) == 'S'){
                morse += "...";
                numberKey += "3";
            }
            else if(input.charAt(i) == 'T'){
                morse += "-";
                numberKey += "1";
            }
            else if(input.charAt(i) == 'U'){
                morse += "..-";
                numberKey += "3";
            }
            else if(input.charAt(i) == 'V'){
                morse += "...-";
                numberKey += "4";
            }
            else if(input.charAt(i) == 'W'){
                morse += ".--";
                numberKey += "3";
            }
            else if(input.charAt(i) == 'X'){
                morse += "-..-";
                numberKey += "4";
            }
            else if(input.charAt(i) == 'Y'){
                morse += "-.--";
                numberKey += "4";
            }
            else if(input.charAt(i) == 'Z'){
                morse += "--..";
                numberKey += "4";
            }
            else if(input.charAt(i) == '_'){
                morse += "..--";
                numberKey += "4";
            }
            else if(input.charAt(i) == ','){
                morse += ".-.-";
                numberKey += "4";
            }
            else if(input.charAt(i) == '.'){
                morse += "---.";
                numberKey += "4";
            }
            else if(input.charAt(i) == '?'){
                morse += "----";
                numberKey += "4";
            }
        }

        return morse + " " + numberKey;
    }

    public static String translate(String morse, String key){
        int counter = key.length()-1;
        int i = 0;
        String returnString = "";
        while(i != morse.length()){
            int keyValue = Integer.parseInt("" + key.charAt(counter));
            String word = morse.substring(i, i + keyValue);

            i += keyValue;
            counter --;

            if(word.equals(".-")){
                returnString += "A";
            }
            else if(word.equals("-...")){
                returnString  += "B";
            }
            else if(word.equals("-.-.")){
                returnString += "C";
            }
            else if(word.equals("-..")){
                returnString += "D";
            }
            else if(word.equals(".")){
                returnString += "E";
            }
            else if(word.equals("..-.")){
                returnString += "F";
            }
            else if(word.equals("--.")){
                returnString += "G";
            }
            else if(word.equals("....")){
                returnString += "H";
            }
            else if(word.equals("..")){
                returnString += "I";
            }
            else if(word.equals(".---")){
                returnString += "J";
            }
            else if(word.equals("-.-")){
                returnString += "K";
            }
            else if (word.equals(".-..")){
                returnString += "L";
            }
            else if(word.equals("--")){
                returnString += "M";
            }
            else if(word.equals("-.")){
                returnString += "N";
            }
            else if(word.equals("---")){
                returnString += "O";
            }
            else if(word.equals(".--.")){
                returnString += "P";
            }
            else if(word.equals("--.-")){
                returnString += "Q";
            }
            else if(word.equals(".-.")){
                returnString += "R";
            }
            else if(word.equals("...")){
                returnString += "S";
            }
            else if(word.equals("-")){
                returnString += "T";
            }
            else if(word.equals("..-")){
                returnString += "U";
            }
            else if(word.equals("...-")){
                returnString += "V";
            }
            else if(word.equals(".--")){
                returnString += "W";
            }
            else if(word.equals("-..-")){
                returnString += "X";
            }
            else if(word.equals("-.--")){
                returnString += "Y";
            }
            else if(word.equals("--..")){
                returnString += "Z";
            }
            else if(word.equals("..--")){
                returnString += "_";
            }
            else if(word.equals(".-.-")){
                returnString += ",";
            }
            else if(word.equals("---.")){
                returnString += ".";
            }
            else if(word.equals("----")){
                returnString += "?";
            }

        }

        return returnString;
    }

    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);
        StringBuilder builder = new StringBuilder();

        while(sc.hasNextLine()){
            String input = sc.nextLine();
            String[] splitt = (morsify(input)).split(" ");
            builder.append(translate(splitt[0], splitt[1]) + "\n");
        }

        //TEST System.out.print(translate(".-", "2"));
        System.out.print(builder.toString());
    }
}
