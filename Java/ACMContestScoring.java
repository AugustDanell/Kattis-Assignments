import java.util.Scanner;

/**
 * Created by August DH on 2016-12-20.
 */
public class ACMContestScoring {
    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);
        boolean run = true;
        StringBuilder builderBob = new StringBuilder();

        int sum = 0;
        int correctAnswers = 0;
        String inCorrectAnswers = "";
        int lastEntry = 0;

        while(run){
            String input = sc.nextLine();
            String[] splittedinput = input.split(" ");
            int minutes = Integer.parseInt(splittedinput[0]);
            if(lastEntry != -1) {
                lastEntry = Integer.parseInt(splittedinput[0]);
            }
            if(minutes == -1){
                run = false;
            }

            if(run && splittedinput[2].equals("right")){
                correctAnswers++;
                sum += minutes;

                for(int i = 0; i < inCorrectAnswers.length(); i++){
                    if(splittedinput[1].charAt(0) == inCorrectAnswers.charAt(i)){
                        sum += 20;
                    }
                }

            }
            else if (run && splittedinput[2].equals("wrong")){
                inCorrectAnswers += splittedinput[1];
            }
        }

        System.out.print(correctAnswers + " " + sum);
    }
}
