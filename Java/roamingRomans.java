import java.util.Scanner;

public class roamingRomans {
    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);
        String inp = sc.nextLine();

        double input = Double.parseDouble(inp);

        double answer = input * 1000 * (5280.0/4854.0);
        System.out.println(Math.round(answer));
    }
}

