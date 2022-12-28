import java.util.*;

public class pokechat {
    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);
        String message = sc.nextLine();
        String encode = sc.nextLine();
        String out = "";

        for(int i = 0; i < encode.length()/3; i++){
            //System.out.println(message.substring(3*i, 3*(i+1)));
            out += message.charAt(Integer.parseInt(encode.substring(3*i, 3*(i+1))) - 1);
        }

        System.out.println(out);
    }
}
