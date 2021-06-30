import java.util.*;
public class asciiAdd{

    public static void main(String []args){
        Scanner sc = new Scanner(System.in);
        String lines[] = new String[7];

        for(int i = 0; i < 7; i++){
            lines[i] = sc.nextLine();
        }
        String concatSum = "";
        int sum = 0;

        for(int i = 0; i < lines[0].length(); i++){
            String[] partString = new String[7];
            for(int j = 0; j < 7; j++){
                partString[j] = lines[j].substring(i, i+5);
            }

            //System.out.println(Arrays.toString(partString));
            concatSum += asciiToString(partString);

            i+= 4;
            if(i != lines[0].length() - 1){
                i++;
            }
        }

        String[] splittedSum = concatSum.split("x");
        sum = sum(splittedSum);
        //System.out.println(sum);
        print(intToAscii(sum));

    }



    //A function that uses a series of helper functions to convert ascii -> int
    public static String asciiToString(String[] in){
        if(isZero(in)){
            return "0";
        }
        else if(isOne(in)){
            return "1";
        }
        else if(isTwo(in)){
            return "2";
        }
        else if(isThree(in)){
            return "3";
        }
        else if(isFour(in)){
            return "4";
        }
        else if(isFive(in)){
            return "5";
        }
        else if(isSix(in)){
            return "6";
        }
        else if(isSeven(in)){
            return "7";
        }
        else if(isEight(in)){
            return "8";
        }
        else if(isNine(in)){
            return "9";
        }

        return "x";
    }

    //A series of helper functions to convert from Ascii art to int:
    public static boolean isZero(String[] in){
        if(in[0].charAt(0) == 'x' && in[0].charAt(4) == 'x' && in[3].charAt(2) == '.'
                && in[6].charAt(0) == 'x' && in[4].charAt(0) == 'x'){
            return true;
        }
        return false;
    }

    public static boolean isOne(String[] in){
        if(in[0].charAt(0) == '.' && in[3].charAt(0) == '.'){
            return true;
        }
        return false;
    }

    public static boolean isTwo(String[] in){
        if(in[0].charAt(0) == 'x' && in[3].charAt(2) == 'x' && in[5].charAt(4) == '.'){
            return true;
        }
        return false;
    }

    public static boolean isThree(String[] in){
        if(in[0].charAt(2) == 'x' && in[3].charAt(0) == 'x' && in[5].charAt(4) == 'x'&& in[5].charAt(0) == '.'
                && in[1].charAt(0) == '.'){
            return true;
        }

        return false;
    }

    public static boolean isFour(String[] in){
        if(in[0].charAt(2) == '.' && in[6].charAt(4) == 'x' && in[0].charAt(0) == 'x'){
            return true;
        }

        return false;
    }

    public static boolean isFive(String[] in){
        if(in[0].charAt(2) == 'x' && in[1].charAt(0) == 'x' && in[1].charAt(4) == '.' && in[4].charAt(0) == '.'){
            return true;
        }
        return false;
    }

    public static boolean isSix(String[] in){
        if(in[0].charAt(2) == 'x' && in[1].charAt(0) == 'x' && in[3].charAt(0) == 'x'
                && in[1].charAt(4) == '.'){
            return true;
        }

        return false;
    }

    public static boolean isSeven(String[] in){
        if(in[0].charAt(2) == 'x' && in[1].charAt(0) == '.' && in[3].charAt(0) == '.'){
            return true;
        }
        return false;
    }

    public static boolean isEight(String[] in){
        if(in[0].charAt(2) == 'x' && in[1].charAt(0) == 'x' && in[1].charAt(4) == 'x' &&
                in[4].charAt(0) == 'x' && in[3].charAt(2) == 'x'){
            return true;

        }
        return false;
    }

    public static boolean isNine(String[] in){
        if(in[0].charAt(2) == 'x' && in[1].charAt(0) == 'x' && in[4].charAt(0) == '.'
                && in[1].charAt(4) == 'x'){
            return true;
        }
        return false;
    }

    public static int sum(String[] in){
        int sum = 0;
        for(int i = 0; i < in.length; i++){
            sum += Integer.parseInt(in[i]);
        }

        return sum;
    }

    public static String[] intToAscii(int integer){
        String in = "" + integer;
        String output[] = new String[7];
        for(int i = 0; i < 7; i++){
            output[i] = ""; //INIT output
        }

        for(int i = 0; i < in.length(); i++){
            //Append for zero
            if(in.charAt(i) == '0'){
                output[0] += "xxxxx";
                output[1] += "x...x";
                output[2] += "x...x";
                output[3] += "x...x";
                output[4] += "x...x";
                output[5] += "x...x";
                output[6] += "xxxxx";
            }
            else if(in.charAt(i) == '1'){
                output[0] += "....x";
                output[1] += "....x";
                output[2] += "....x";
                output[3] += "....x";
                output[4] += "....x";
                output[5] += "....x";
                output[6] += "....x";
            }
            else if(in.charAt(i) == '2'){
                output[0] += "xxxxx";
                output[1] += "....x";
                output[2] += "....x";
                output[3] += "xxxxx";
                output[4] += "x....";
                output[5] += "x....";
                output[6] += "xxxxx";
            }
            else if(in.charAt(i) == '3'){
                output[0] += "xxxxx";
                output[1] += "....x";
                output[2] += "....x";
                output[3] += "xxxxx";
                output[4] += "....x";
                output[5] += "....x";
                output[6] += "xxxxx";
            }

            else if(in.charAt(i) == '4'){
                output[0] += "x...x";
                output[1] += "x...x";
                output[2] += "x...x";
                output[3] += "xxxxx";
                output[4] += "....x";
                output[5] += "....x";
                output[6] += "....x";
            }

            else if(in.charAt(i) == '5'){
                output[0] += "xxxxx";
                output[1] += "x....";
                output[2] += "x....";
                output[3] += "xxxxx";
                output[4] += "....x";
                output[5] += "....x";
                output[6] += "xxxxx";
            }
            if(in.charAt(i) == '6'){
                output[0] += "xxxxx";
                output[1] += "x....";
                output[2] += "x....";
                output[3] += "xxxxx";
                output[4] += "x...x";
                output[5] += "x...x";
                output[6] += "xxxxx";
            }
            else if(in.charAt(i) == '7'){
                output[0] += "xxxxx";
                output[1] += "....x";
                output[2] += "....x";
                output[3] += "....x";
                output[4] += "....x";
                output[5] += "....x";
                output[6] += "....x";
            }
            if(in.charAt(i) == '8'){
                output[0] += "xxxxx";
                output[1] += "x...x";
                output[2] += "x...x";
                output[3] += "xxxxx";
                output[4] += "x...x";
                output[5] += "x...x";
                output[6] += "xxxxx";
            }
            if(in.charAt(i) == '9'){
                output[0] += "xxxxx";
                output[1] += "x...x";
                output[2] += "x...x";
                output[3] += "xxxxx";
                output[4] += "....x";
                output[5] += "....x";
                output[6] += "xxxxx";
            }

            if(i != in.length() - 1){
                for(int j = 0; j < 7; j++){
                    output[j] += ".";
                }
            }
        }
        return output;
    }

    public static void print(String[] in){
        for(int i = 0; i < 7; i++){
            System.out.println(in[i]);
        }
    }

}