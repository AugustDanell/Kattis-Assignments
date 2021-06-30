import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

/**
 * Created by August DH on 2016-12-24.
 */
public class BaconEggsandSpam {
    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);
        boolean run = true;
        StringBuilder builderBob = new StringBuilder();

        while(run){
            String cases = sc.nextLine();
            String[] splittedCases = cases.split(" ");
            int numberOfCases = Integer.parseInt(splittedCases[0]);

            if(numberOfCases != 0){
                ArrayList<String> names = new ArrayList<>();
                ArrayList<String> items = new ArrayList<>();
                ArrayList<String> completeString = new ArrayList<>();

                for(int i = 0; i < numberOfCases; i++){
                    String input = sc.nextLine();
                    String[] splittedInput = input.split(" ");

                    completeString.add(input);

                    for(int j = 0; j<splittedInput.length; j++){
                        if((int)splittedInput[j].charAt(0) >= 65 && (int)splittedInput[j].charAt(0) <= 90 && !names.contains(splittedInput[j])){
                            names.add(splittedInput[j]);
                        }

                        if(j!= 0 && !items.contains(splittedInput[j])){
                            items.add(splittedInput[j]);
                        }
                    }

                    //Insertion sort for sorting the items lexiographically
                    java.util.Collections.sort(items);
                    /*for(int j = 1; j < items.size(); j++){
                        String x = items.get(j);
                        int k = j - 1;
                        while(k >= 0 && (int)items.get(k).charAt(0) > (int)x.charAt(0)){
                            items.set(k+1, items.get(k));
                            k = k - 1;
                        }
                        items.set(k+1, x);
                    }*/
                }

                //System.out.print(items);

                for(int i = 0; i < items.size(); i++){
                    ArrayList<String> listOfNames = new ArrayList<>();
                    builderBob.append(items.get(i));
                    for(int j = 0; j < completeString.size(); j++){
                        if(completeString.get(j).contains(items.get(i))){
                            //builderBob.append(" " + names.get(j));
                            listOfNames.add( names.get(j));
                        }
                    }
                    Collections.sort(listOfNames);

                    for(int j = 0; j < listOfNames.size(); j++){
                        builderBob.append(" " + listOfNames.get(j));
                    }

                    builderBob.append("\n");
                }

                //System.out.print(items);
                builderBob.append("\n");
            }
            else{
                run = false;
            }
        }

        System.out.print(builderBob.toString());
    }
}
