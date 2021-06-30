import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

/**
 * Created by August DH on 2017-03-07.
 */
public class plantingTrees2 {
    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);
        ArrayList<Integer> list = new ArrayList<>();

        int trees = sc.nextInt();
        sc.nextLine();

        String seedlings = sc.nextLine();
        String[] splitted = seedlings.split(" ");
        for(int i = 0; i < splitted.length; i++){
            list.add(Integer.parseInt(splitted[i]));
        }
        Collections.sort(list);

        int day = 1;
        int largestDay = 0;
        for(int i = list.size()-1; i >= 0; i--){
            if((day + list.get(i)) > largestDay){
                largestDay = (day + list.get(i));
            }
            day++;
        }

        System.out.print(largestDay + 1);
    }
}
