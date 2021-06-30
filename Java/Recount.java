import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

/**
 * Created by August DH on 2017-02-03.
 */
public class Recount {
    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);
        boolean run = true;
        boolean runOff = false;
        String bestCandidate = "";
        ArrayList<String> nameList = new ArrayList<>();

        while(run){
            String input = sc.nextLine();
            if(!input.equals("***")){
                nameList.add(input);
            }
            else{
                //Sorts the array once *** is inputed
                Collections.sort(nameList);

                String candidate = nameList.get(0);
                bestCandidate = nameList.get(0);
                int mostVotes = 1;
                int votes = 1;

                //System.out.println(nameList);
                for(int i = 1; i < nameList.size(); i++){
                    if(candidate.equals(nameList.get(i))){
                        votes ++;

                        if(votes == mostVotes){
                            runOff = true;
                        }

                        if(votes > mostVotes){
                            mostVotes = votes;
                            bestCandidate = nameList.get(i);
                            runOff = false;
                        }
                    }
                    else{
                       // System.out.print("Votes: " + votes);
                        candidate = nameList.get(i);
                        votes = 1;

                        if(votes == mostVotes){
                            runOff = true;
                        }
                    }

                    //index ++;
                }

                run = false;
            }
        }

        if(!runOff){
            System.out.println(bestCandidate);
        }
        else{
            System.out.println("Runoff!");
        }
    }
}
