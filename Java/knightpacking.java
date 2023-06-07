import java.util.Scanner;

public class knightpacking{
    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        if(a % 2 == 0){
            System.out.println("second");
        }
        else{
            System.out.println("first");
        }
    }
}
