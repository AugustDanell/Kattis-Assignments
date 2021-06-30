import java.util.Scanner;

/**
 * Created by August DH on 2017-02-25.
 */
public class BestComprise {
    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);
        int cases = sc.nextInt();
        sc.nextLine();
        StringBuilder builder = new StringBuilder();

        for(int i = 0; i< cases; i++){
            String input = sc.nextLine();
            String[] splittedInput = input.split(" ");
            int persons = Integer.parseInt(splittedInput[0]);
            int answers = Integer.parseInt(splittedInput[1]);

            int[] answerCount = new int[answers];
            for(int j = 0; j < persons; j++){
                String answerInput = sc.nextLine();

                for(int k = 0; k < answers; k++){
                    if(answerInput.charAt(k) == '1'){
                        answerCount[k] += 1;
                    }
                    else{
                        answerCount[k] -= 1;
                    }
                }
            }
            for(int j = 0; j < answers; j++){
                if(answerCount[j] >= 1){
                    builder.append("1");
                }
                else{
                    builder.append("0");
                }
            }
            builder.append("\n");
        }
        System.out.print(builder.toString());
    }
}
