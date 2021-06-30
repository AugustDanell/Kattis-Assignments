import java.util.ArrayList;
import java.util.Scanner;

/**
 * Created by August DH on 2017-04-04.
 */
public class secureDoors2 {
    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);
        int cases = sc.nextInt();
        sc.nextLine();
        StringBuilder builder = new StringBuilder();

        ArrayList<String> inside = new ArrayList<>();


        for(int i = 0; i < cases; i++){
            String entryInput = sc.nextLine();
            boolean entry = false;
            boolean anomaly = false;

            String[] splitted = entryInput.split(" ");
            if(splitted[0].equals("entry")){
                entry = true;
            }

            if(entry && inside.contains(splitted[1])){
                anomaly = true;
            }
            else if(!entry && !inside.contains(splitted[1])){
                anomaly = true;
            }

            if(!anomaly && entry){
                builder.append(splitted[1] + " entered\n");
                inside.add(splitted[1]);
            }
            else if(!anomaly && !entry){
                builder.append(splitted[1] + " exited\n");
                inside.remove(splitted[1]);
            }
            else if(anomaly && entry){
                builder.append(splitted[1] + " entered (ANOMALY)\n");
            }
            else{
                builder.append(splitted[1] + " exited (ANOMALY)\n");
            }
        }
        System.out.print(builder.toString());
    }
}
