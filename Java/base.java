import java.util.Scanner;
// Kattis ID: whichbase

public class base {
    public static long oct(String inp){
        if (inp.contains("9") || inp.contains("8")){
            return 0;
        }
        else{
            // Specifiera bas i parsningen
            return Long.parseLong(inp, 8);
        }
    }

    public static long hex(String inp){
        return Long.parseLong(inp, 16);
    }

    public static String trimtrim(String inp){
        if(inp.charAt(0) == '0' && inp.length() > 1){
            return trimtrim(inp.substring(1));
        }
        else {
            return inp;
        }
    }

    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);
        int tests = sc.nextInt();
        sc.nextLine();
        StringBuilder bob = new StringBuilder();

        for(int i = 0; i < tests; i++){
          String input = sc.nextLine();
          String[] split = input.split(" ");

          bob.append(split[0] + " ");
          bob.append(oct(split[1]) + " ");
          bob.append(trimtrim(split[1]) + " ");
          bob.append(hex(split[1]));
          bob.append("\n");
        }

        System.out.println(bob.toString());
    }
}
