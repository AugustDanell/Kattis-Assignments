import java.util.Scanner;

/**
 * Created by August DH on 2016-12-13.
 */
public class OddManOut {
    public static void main(String[]args){
        Scanner sc = new Scanner (System.in);

        StringBuilder builderBob = new StringBuilder();
        String cases = sc.nextLine();
        String[] splittedCase = cases.split(" ");
        int numberOfCases = Integer.parseInt(splittedCase[0]);

        for (int i = 0; i < numberOfCases; i++){
            String G = sc.nextLine();
            String idOfGuests = sc.nextLine();

            String[] splittedIdOfGuests = idOfGuests.split(" ");
            int[] GuestIDs = new int[splittedIdOfGuests.length];

            for(int j = 0; j<splittedIdOfGuests.length; j++){
                GuestIDs[j] = Integer.parseInt(splittedIdOfGuests[j]);
            }


            boolean shouldBeKickedOut[] = new boolean[splittedIdOfGuests.length];
            for(int j = 0; j < splittedIdOfGuests.length; j++){
                shouldBeKickedOut[j] = true;
            }

        for(int k = 0; k < splittedIdOfGuests.length; k++) {
            for (int j = 0; j < splittedIdOfGuests.length; j++) {
                if (k != j && GuestIDs[k] == GuestIDs[j]) {
                    shouldBeKickedOut[k] = false;
                }
            }
        }

            for(int j = 0; j < splittedIdOfGuests.length; j++){
                if(shouldBeKickedOut[j]){
                    builderBob.append("Case #" + (i+1) + ": " + GuestIDs[j] + "\n");
                }
            }
        }

        System.out.print(builderBob.toString());
    }
}
