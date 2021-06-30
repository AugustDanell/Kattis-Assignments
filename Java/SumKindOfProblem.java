import java.util.Scanner;

/**
 * Created by August DH on 2016-12-16.
 */
public class SumKindOfProblem {
    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);
        StringBuilder builder = new StringBuilder();

        String input = sc.nextLine();
        String[] splittedInput = input.split(" ");
        int P = Integer.parseInt(splittedInput[0]);
        String printString = "";

        for(int i = 0; i < P; i++){
            String lineInput = sc.nextLine();
            String[] splittedLineInput = lineInput.split(" ");

            int K = Integer.parseInt(splittedLineInput[0]);
            int N = Integer.parseInt(splittedLineInput[1]);

            int S1 = 0;
            int S2 = 0;
            int S3 = 0;

            //Doing the calculations for S1.
            for(int j = 0; j <= N; j++){
                S1 += j;
            }

            //Doing the calculations for S2 and S3.
            for(int j = 0; j <= N*2; j++){
                if(j%2==1){
                    S2 += j;
                }
                else if(j%2 == 0){
                    S3 += j;
                }
            }
            builder.append(K + " " + S1 + " " + S2 + " " + S3 + "\n");

            //printString += K + " " + S1 + " " + S2 + " " + S3 + "\n";
        }

        System.out.print(builder.toString());
    }
}
