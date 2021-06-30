import java.util.Scanner;

public class hangingOutOnTheTerrace {
    public static int leave(int current, int people){
        return current - people;
    }


    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);
        String input = sc.nextLine();
        String[] splitted = input.split(" ");

        int L = Integer.parseInt(splitted[0]);
        int events = Integer.parseInt(splitted[1]);

        int groupForbidden = 0;
        int currentPeople = 0;
        for(int i = 0; i < events; i++){
            String groupInput = sc.nextLine();
            String split[] = groupInput.split(" ");
            int people = Integer.parseInt(split[1]);

            if(split[0].equals("enter")){
                // How many people entering.
                if(people + currentPeople <= L){
                    currentPeople += people;
                }
                else {
                    groupForbidden ++;
                }
            }
            else{
                //Must equal leave
                currentPeople -= people;
            }
        }

        System.out.println(groupForbidden);
    }
}
