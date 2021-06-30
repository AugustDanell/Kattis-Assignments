import java.util.Scanner;

/**
 * Created by August DH on 2017-03-07.
 */
public class trollHunt {
    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);
        String input = sc.nextLine();
        String[] splitted = input.split(" ");

        int bridges = Integer.parseInt(splitted[0]) -1; //Filthy troll hideouts.
        int knights = Integer.parseInt(splitted[1]);    //Brothers sworn into the holy order
        int groupMembers = Integer.parseInt(splitted[2]);

        int knightGroups = 0;
        //Forming groups of knights to clear the out the blasphemous troll Den. DEUS VULT.
        while(knights >= groupMembers){
            knightGroups ++;
            knights -= groupMembers;
        }

        int daysSearched = 0;
        //Purging bridges like the Spanish F****** Inquisition. DEUS VULT.
        while(bridges > 0){
            daysSearched ++;
            bridges -= knightGroups;
        }

        System.out.print(daysSearched);
    }
}
