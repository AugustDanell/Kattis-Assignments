import java.util.Scanner;
// Problem ID: Tetration
public class limits {
    public static double tetration(double d){
        double N = d;
        return Math.pow(d, 1/N);
    }

    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);
        String inp = sc.nextLine();
        double d = Double.parseDouble(inp);

        System.out.println(tetration(d));
    }
}
