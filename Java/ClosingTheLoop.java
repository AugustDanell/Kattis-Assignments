import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

/**
 * Created by August DH on 2017-02-14.
 */
public class ClosingTheLoop {
    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);
        StringBuilder builder = new StringBuilder();

        int cases = sc.nextInt();
        sc.nextLine();

        for(int i = 0; i < cases; i++) {
            int ropeLength = 0;

            builder.append("Case #" + (i + 1) + ": ");
            ArrayList<Integer> redRopes = new ArrayList<>();
            ArrayList<Integer> brownRopes = new ArrayList<>();

            int NumberOfRopes = sc.nextInt();
            sc.nextLine();

            String input = sc.nextLine();
            String[] splittedInput = input.split(" ");

            for (int j = 0; j < splittedInput.length; j++) {
                if (splittedInput[j].charAt(splittedInput[j].length() - 1) == 'R') {
                    redRopes.add(Integer.parseInt(splittedInput[j].substring(0, splittedInput[j].length() - 1)));
                } else {
                    brownRopes.add(Integer.parseInt(splittedInput[j].substring(0, splittedInput[j].length() - 1)));
                }
            }

            Collections.sort(redRopes);
            Collections.sort(brownRopes);

            if (redRopes.size() == 0 || brownRopes.size() == 0) {
                builder.append(ropeLength + "\n");
            } else {

                while (redRopes.size() != 0 && brownRopes.size() != 0) {
                    ropeLength += redRopes.get(redRopes.size() - 1) + brownRopes.get(brownRopes.size() - 1) - 2;
                    redRopes.remove(redRopes.size() - 1);
                    brownRopes.remove(brownRopes.size() - 1);

                }

                //System.out.println(ropeLength);
                builder.append(ropeLength + "\n");
            }

        }

        System.out.print(builder.toString());
    }
}
