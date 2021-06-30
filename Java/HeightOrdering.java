import java.util.Arrays;
import java.util.Scanner;

/**
 * Created by August DH on 2016-12-17.
 */
public class HeightOrdering {
    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);
        String caseInput = sc.nextLine();
        String[] splittedCaseInput = caseInput.split(" ");
        int cases = Integer.parseInt(splittedCaseInput[0]);
        StringBuilder builderBob = new StringBuilder();

        for(int i = 0; i<cases; i++){
            String heightInput = sc.nextLine();
            String[] inputedHeightInputs = heightInput.split(" ");

            int[] heights = new int[20];
            for(int j = 1; j <= 20; j++){
                heights[j-1] = Integer.parseInt(inputedHeightInputs[j]);
            }
            //System.out.print(Arrays.toString(heights));

            int iterationSwaps = 0;
            for(int j = 1; j < 20; j++){
                int x = heights[j];
                int k = j-1;

                while(k >= 0 && heights[k] > x){
                    heights[k+1] = heights[k];
                    k = k - 1;
                    iterationSwaps ++;
                }
                heights[k+1] = x;
            }
            builderBob.append((i+1) + " " + iterationSwaps + "\n");
            //System.out.print(iterationSwaps);
        }

        System.out.print(builderBob.toString());
    }
}
