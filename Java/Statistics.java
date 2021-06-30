import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

/**
 * Created by August DH on 2016-12-14.
 */
public class Statistics {
    public static void main(String[]args){
        Scanner sc = new Scanner (System.in);
        String input = "";//sc.nextLine();
        StringBuilder builderBob = new StringBuilder();
        int i = 0;
        while(sc.hasNextLine()){
            //if(i!=0){
                input = sc.nextLine();
            //}
            String[] integers = input.split(" ");
            ArrayList<Integer> list = new ArrayList<>();

            for(int j = 1; j < integers.length; j++){
                list.add(Integer.parseInt(integers[j]));
            }

            Collections.sort(list);
            int min = list.get(0);
            int max = list.get(list.size()-1);
            int range = max - min;
            int currentCase = i+1;
            i++;

            builderBob.append("Case " + currentCase +": " + min + " " + max + " " + range + "\n");
        }

        System.out.print(builderBob.toString());
    }
}
