import java.util.ArrayList;
import java.util.Scanner;

/**
 * Created by August DH on 2017-08-13.
 */
public class numbersOnATree {
    public static void main(String args []) {
        Scanner sc = new Scanner(System.in);
        String input = sc.nextLine();
        String[] splitted = input.split(" ");

        long root = Long.parseLong(splitted[0]);
        root = (long) Math.pow(2, root+1) - 1;
        long current = root;
        String traveral = "";
        if (splitted.length > 1){
            traveral = splitted[1];
        }

        long depth = 1;
        ArrayList<Long> savedTraversals = new ArrayList<>();

        for(int i = 0; i < traveral.length(); i++){
            if(traveral.charAt(i) == 'R'){
                current -= (long)Math.pow(2, depth);
            }
            else if (traveral.charAt(i) == 'L'){
                current -= (long)Math.pow(2, depth); //Kodduplicering
                savedTraversals.add(depth);
            }
            depth ++;
        }

        for(int i = 0; i < savedTraversals.size(); i++){
            current += (long)Math.pow(2, (depth-savedTraversals.get(i) - 1));
        }

        System.out.print(current);
    }
}
