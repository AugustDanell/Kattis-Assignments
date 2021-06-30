import java.util.ArrayList;
import java.util.Scanner;
// Saving Princess Peach

public class mario {
    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);
        String input = sc.nextLine();
        String split[] = input.split(" ");

        int N = Integer.parseInt(split[0]);
        int Y = Integer.parseInt(split[1]);
        StringBuilder bob = new StringBuilder();
        ArrayList listOfDoneObs = new ArrayList<Integer>();
        int found = 0;

        for(int i = 0; i < Y; i++){
            int obst = sc.nextInt();
            sc.nextLine();

            if(!listOfDoneObs.contains(obst)) {
                listOfDoneObs.add(obst);
                found ++;
            }
        }

        for(int i = 0; i < N; i++){
            if(!listOfDoneObs.contains(i))
            System.out.println(i);
        }

        System.out.print("Mario got " + found + " of the dangerous obstacles.");
    }
}
