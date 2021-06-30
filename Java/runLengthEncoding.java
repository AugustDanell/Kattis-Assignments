import java.util.Scanner;
// Problem ID: Runlengthencodingrun

public class runLengthEncoding {
    public static String encode(String in){
        String ret = "";
        char prev = 'ö';
        in += "ö"; //Lazy

        boolean bind = false;
        int count = 1;

        for(int i = 0; i < in.length(); i++){
            if(in.charAt(i) == prev){
                bind = true;
                count ++;
            }
            else if(bind){
                ret += "" + prev + count;
                bind = false;
                count = 1;
            }
            else{
                if(prev != 'ö'){
                    ret += "" + prev + count;
                }
            }

            prev = in.charAt(i);
        }

        return ret;
    }

    public static String decode(String in){
        String ret = "";
        for(int i = 0; i < in.length(); i+= 2){
            int chars = Integer.parseInt("" + in.charAt(i+1));
            for(int j = 0; j < chars; j++){
                ret += "" + in.charAt(i);
            }
        }

        return ret;
    }

    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);
        String input = sc.nextLine();
        String[] split = input.split(" ");

        if(split[0].equals("E")){
            System.out.println(encode(split[1]));
        }
        else{
            System.out.println(decode(split[1]));
        }
    }
}
