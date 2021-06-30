import java.text.DecimalFormat;
import java.util.Scanner;

/**
 * Created by August DH on 2017-06-25.
 */
public class vaccumba2 {
    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);
        int tests = sc.nextInt();
        sc.nextLine();


        StringBuilder builder = new StringBuilder();
        for(int i = 0; i < tests; i++){
            double x = 0;
            double y = 0;
            double degree = 90;

            int segments = sc.nextInt();
            sc.nextLine();

            for(int j = 0; j < segments; j++){
                String segment = sc.nextLine();
                String[] splittedSegment = segment.split(" ");
                double distance = Double.parseDouble(splittedSegment[1]);

                degree += Double.parseDouble(splittedSegment[0]) % 360;
                x += distance * Math.cos(Math.toRadians(degree));
                y += distance * Math.sin(Math.toRadians(degree));
            }

            DecimalFormat numberFormat = new DecimalFormat("#.000000");
            String appendage = numberFormat.format(x) + " " + numberFormat.format(y) + "\n";
            appendage = appendage.replaceAll(",", ".");
            builder.append(appendage);
        }

        System.out.print(builder.toString());
    }
}
