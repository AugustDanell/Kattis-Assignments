import java.util.Scanner;
// Solution to Chanukah Challenge
public class Chanukah {
    public static int sumFac(int n){
        if(n == 0){
            return 0;
        }
        else{
            return n + sumFac(n-1);
        }
    }

    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);
        int cases = sc.nextInt();
        sc.nextLine();

        StringBuilder bob = new StringBuilder();

        for(int i = 0; i < cases; i++){
            String input = sc.nextLine();
            String[] split = input.split(" ");
            int days = Integer.parseInt(split[1]);

            bob.append(split[0] + " " + (days + sumFac(days)) + "\n");
        }

        System.out.print(bob.toString());
    }
}
