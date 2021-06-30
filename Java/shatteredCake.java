import java.util.Scanner;

public class shatteredCake {
    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);
        int width = sc.nextInt();
        sc.nextLine();

        int pieces = sc.nextInt();
        sc.nextLine();

        int area = 0;
        for(int i = 0; i < pieces; i++){
            String input = sc.nextLine();
            String[] split = input.split(" ");

            area += Integer.parseInt(split[0]) * Integer.parseInt(split[1]);
        }

        System.out.println(area / width);
    }
}
