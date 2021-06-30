import java.lang.Math;
import java.util.*;
// Solution to Babylonian Numbers
public class babylonian
{
    public static StringBuilder bob = new StringBuilder();
    public static void main(String[] args)
    {
        Scanner sc = new Scanner (System.in);
        int cases = sc.nextInt();
        sc.nextLine();

        for(int i = 0; i < cases; i++){
            String input = sc.nextLine();
            input = process(input);

            babylon(input);
        }
        System.out.println(bob.toString());
    }

    public static void babylon(String in){
        long sum = 0;

        String[] splitted = in.split(",");
        //System.out.println(in);

        for(int i = 0; i < splitted.length; i++){
            int a = Integer.parseInt(splitted[splitted.length-1-i]);
            sum += Math.pow(60, i) * a;
        }
        bob.append(sum + "\n");
        //System.out.println(sum);
    }

    public static String process(String in){
        if(in.charAt(in.length() - 1) == ','){
            in += "0";
        }
        for(int i = 0; i < 10; i++){
            in = in.replaceAll(",,", ",0,");
        }
        return in;
    }
}

