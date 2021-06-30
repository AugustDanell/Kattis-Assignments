import java.util.Arrays;
import java.util.Scanner;

/**
 * Created by August DH on 2016-12-11.
 */
public class Ptice {
    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);
        int questions = sc.nextInt();
        sc.nextLine();
        String inputedSequence;
        String[] partcipatingAnswers = new String[3];
        String[] participatingPersons = {"Adrian", "Bruno", "Goran"};
        int[] counter = new int[3];

        //Defines the strings
        partcipatingAnswers[0] = "";
        partcipatingAnswers[1] = "";
        partcipatingAnswers[2] = "";

        //Generates the answer paterns
        for(int i = 0; i < questions; i++){
            if(i%3 == 0){
                partcipatingAnswers[0] += "A";
            }
            if(i%3 == 1){
                partcipatingAnswers[0] += "B";
            }
            if(i%3 == 2){
                partcipatingAnswers[0] += "C";
            }
        }


        for(int i = 0; i < questions; i++){
            if(i%4 == 0){
                partcipatingAnswers[1] += "B";
            }
            if(i%4 == 1){
                partcipatingAnswers[1] += "A";
            }
            if(i%4 == 2){
                partcipatingAnswers[1] += "B";
            }
            if(i%4 == 3){
                partcipatingAnswers[1] += "C";
            }
        }

        for(int i = 0; i < questions; i++){
            if(i%6 == 0){
                partcipatingAnswers[2] += "C";
            }
            if(i%6 == 1){
                partcipatingAnswers[2] += "C";
            }
            if(i%6 == 2){
                partcipatingAnswers[2] += "A";
            }
            if(i%6 == 3){
                partcipatingAnswers[2] += "A";
            }
            if(i%6 == 4){
                partcipatingAnswers[2] += "B";
            }
            if(i%6 == 5){
                partcipatingAnswers[2] += "B";
            }
        }


        //System.out.println(Arrays.toString(partcipatingAnswers));

        inputedSequence = sc.nextLine();

        //System.out.println(inputedSequence);

        //Incrementing every correctly answered question.
        for(int i = 0; i<questions; i++){
            if(partcipatingAnswers[0].charAt(i) == inputedSequence.charAt(i)){
                counter[0]++;
            }
            if(partcipatingAnswers[1].charAt(i) == inputedSequence.charAt(i)){
                counter[1]++;
            }
            if(partcipatingAnswers[2].charAt(i) == inputedSequence.charAt(i)){
                counter[2]++;
            }
        }

        //System.out.println(Arrays.toString(counter));


        //Comparing the inputed answers and the increments to determine the boy's correctly answered questions
        //And listing them

        for(int i = 0; i < counter.length; i++){
            int x = counter[i];
            String y = participatingPersons[i];

            int j = i -1;
            while(j >= 0 && counter[j]>x){
                counter[j+1] = counter[j];
                participatingPersons[j+1] = participatingPersons[j];
                j = j -1;
            }
            counter[j+1] = x;
            participatingPersons[j+1] = y;
        }

        System.out.println(counter[2]);
        if(counter[0] == counter[2]){
            System.out.println(participatingPersons[0]);
        }
        if(counter[1] == counter[2]){
            System.out.println(participatingPersons[1]);
        }
        System.out.println(participatingPersons[2]);


    }
}
