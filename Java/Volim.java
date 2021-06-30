import java.util.Scanner;

/**
 * Created by August DH on 2016-12-14.
 */
public class Volim {
    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);
        String playerStart = sc.nextLine();
        String[] splittedPlayerStart = playerStart.split(" ");
        int start = Integer.parseInt(splittedPlayerStart[0]);
        int overallTime = 0;

        String question = sc.nextLine();
        String[] splittedQuestions = question.split(" ");
        int questions = Integer.parseInt(splittedQuestions[0]);

        for(int i = 0; i<questions; i++){
            String answer = sc.nextLine();
            String[] splittedAnswer = answer.split(" ");
            String answeredQuestion = splittedAnswer[1];

            String elapsedTime = splittedAnswer[0];
            int time = Integer.parseInt(elapsedTime);
            overallTime += time;

            //System.out.println(answeredQuestion.charAt(0));

            if(answeredQuestion.charAt(0) == 'T' && overallTime < 210){
                start = (start +1)%9;
                if(start == 0){
                    start = 1;
                }
            }
        }
        System.out.println(start);
    }
}
