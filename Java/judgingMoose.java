import java.util.Scanner;

public class judgingMoose {
    public static int max(int a, int b){
        if(a >= b){
            return a+a;
        }
        else{
            return b+b;
        }
    }

    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);
        String input = sc.nextLine();
        if(input.equals("0 0")){
            System.out.println("Not a moose");
        }
        else{
            String[] splitted = input.split(" ");
            int a = Integer.parseInt(splitted[0]);
            int b = Integer.parseInt(splitted[1]);

            if(a != b){
              System.out.println("Odd "+ max(a,b));
            }
            else{
              System.out.println("Even " + max(a,b));
            }
        }
    }
}
