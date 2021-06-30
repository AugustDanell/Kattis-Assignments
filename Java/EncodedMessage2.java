import java.util.Scanner;

/**
 * Created by August DH on 2017-02-17.
 */
public class EncodedMessage2 {
    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);
        int cases = sc.nextInt();
        sc.nextLine();

        StringBuilder builder = new StringBuilder();
        for(int i = 0; i < cases; i++){
            String input = sc.nextLine();
            int modCounter = 0;
            int squareRoot = (int)Math.sqrt(input.length());
            int alignedIndex = 0;

            for(int j = 0; j < squareRoot; j++){
                for(int k = 0; k < squareRoot; k++) {
                    builder.append("" + input.charAt(k*squareRoot+ (squareRoot-j-1)));
                }
            }

            builder.append("\n");
        }

        System.out.print(builder.toString());
    }
}
