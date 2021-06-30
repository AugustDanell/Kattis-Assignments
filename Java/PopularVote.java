import java.util.Scanner;

/**
 * Created by August DH on 2016-12-18.
 */
public class PopularVote {
    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);
        String caseInput = sc.nextLine();
        String[] splittedCaseInput = caseInput.split(" ");
        StringBuilder builderBob = new StringBuilder();


        int cases = Integer.parseInt(splittedCaseInput[0]);
        for(int i = 0; i < cases; i++){
            int numberOfCandidates = sc.nextInt();
            sc.nextLine();
            int[] votes = new int [numberOfCandidates];
            boolean[] existsLarger = new boolean[numberOfCandidates];
            boolean winner = false;
            int voteCount = 0;

            for(int j = 0; j < numberOfCandidates; j++){
                int numberOfVotes = sc.nextInt();
                sc.nextLine();
                votes[j] = numberOfVotes;
                existsLarger[j] = false;
                voteCount += numberOfVotes;

            }

            for(int j = 0; j < numberOfCandidates; j++){
                for(int k = 0; k < numberOfCandidates; k++){
                    if(j != k && votes[j] <= votes[k]){
                        existsLarger[j] = true;
                    }
                }
            }

            //int requiredMajority = (int)Math.ceil(voteCount/2);
            for(int j = 0; j < numberOfCandidates; j++){
                if(!existsLarger[j]){
                    winner = true;
                    int restVote = voteCount-votes[j];

                    if(votes[j] - restVote > 0){
                        builderBob.append("majority winner " + (j+1) + "\n");
                    }
                    else{
                        builderBob.append("minority winner " + (j+1) + "\n");
                    }
                }
            }

            if(!winner){
                builderBob.append("no winner" + "\n");
            }

        }
     System.out.print(builderBob.toString());
    }
}
