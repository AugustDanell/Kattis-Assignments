import java.text.DecimalFormat;
import java.util.Scanner;
// Quality Adjusted Year
public class QALY2 {
    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        sc.nextLine();  // Getting rid of rest of the line

        double sum = 0.0;
        for(int i = 0; i < N; i++) {
            String inp = sc.nextLine();
            String[] split = inp.split(" ");

            sum += Double.parseDouble(split[0]) * Double.parseDouble(split[1]);
        }
        DecimalFormat df = new DecimalFormat("#.####");
        System.out.print((df.format(sum).toString()).replace(",", "."));
    }
}
