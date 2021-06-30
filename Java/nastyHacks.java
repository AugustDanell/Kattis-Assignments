import java.util.Scanner;

/**
 * Created by August DH on 2017-09-15.
 */
public class nastyHacks {
    public static void advertise(String input){
        String[] splitted = input.split(" ");
        int r = Integer.parseInt(splitted[0]);
        int e = Integer.parseInt(splitted[1]);
        int c = Integer.parseInt(splitted[2]);

        int adRev = e - c;

        if(r > adRev){
            System.out.println("do not advertise");
        }
        else if(r == adRev){
            System.out.println("does not matter");
        }
        else{
            System.out.println("advertise");
        }
    }

    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);
        int cases = sc.nextInt();
        sc.nextLine();

        for(int i = 0; i < cases; i++){
            String input = sc.nextLine();
            advertise(input);
        }
    }
}
