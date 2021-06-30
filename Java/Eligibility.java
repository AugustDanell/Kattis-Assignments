import java.util.Scanner;

/**
 * Created by August DH on 2016-12-14.
 */
public class Eligibility {
    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);
        String contestants = sc.nextLine();
        String[]splittedContestantInput = contestants.split(" ");
        int cases = Integer.parseInt(splittedContestantInput[0]);
        String printString = "";

        for(int i = 0; i < cases; i++){
            String contestant = sc.nextLine();
            String[] splitContestant = contestant.split(" ");

            String name = splitContestant[0];

            String beginningOfStudies = splitContestant[1];
            int beginningYear = Integer.parseInt(splitContestant[1].substring(0,4));

            String birth = splitContestant[2];
            int birthYear = Integer.parseInt(splitContestant[2].substring(0, 4));

            //System.out.println(beginningYear);

            int courses = Integer.parseInt(splitContestant[3]);


            if(beginningYear >= 2010){
                printString += name + " eligible" + "\n";
            }

            else if(birthYear >= 1991){
                printString += name + " eligible" + "\n";
            }
            if(courses >= 41 && beginningYear < 2010 && birthYear < 1991){
                printString += name + " ineligible" + "\n";
            }
            if(beginningYear < 2010 && birthYear < 1991 && courses < 41){
                printString += name + " coach petitions" + "\n";
            }

        }

        System.out.print(printString);
    }
}
