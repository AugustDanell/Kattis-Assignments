import java.util.Scanner;

public class railRoad {
    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);
        String input = sc.nextLine();
        String[] splitted = input.split(" ");

        int x = Integer.parseInt(splitted[0]);
        int y = Integer.parseInt(splitted[1]);

        if(y % 2 == 0){
            System.out.println("possible");
        }
        else{
            System.out.println("impossible");
        }
    }
}
