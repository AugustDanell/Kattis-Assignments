import java.util.Scanner;

/**
 * Created by August DH on 2016-12-17.
 */
public class DetailedDifferences {
    public static void main(String[]args) {
        Scanner sc = new Scanner(System.in);
        String cases = sc.nextLine();
        String[] splittedCases = cases.split(" ");
        StringBuilder builderBob = new StringBuilder();

        int numberOfCases = Integer.parseInt(splittedCases[0]);

        for(int i = 0; i < numberOfCases; i++){
            String inputTextOne = sc.nextLine();
            String inputTextTwo = sc.nextLine();

            builderBob.append(inputTextOne + "\n");
            builderBob.append(inputTextTwo + "\n");

            for(int j = 0; j < inputTextOne.length(); j++){
                if(inputTextOne.charAt(j) == inputTextTwo.charAt(j)){
                    builderBob.append(".");
                }
                else{
                    builderBob.append("*");
                }
            }

            builderBob.append("\n" + "\n");
        }

        System.out.print(builderBob.toString());
    }
}
