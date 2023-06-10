import java.util.Scanner;
public class addingtrouble{
    public static void main(String[]args){
        int a;
        int b;
        int c;
        Scanner sc = new Scanner(System.in);
        String[] s = sc.nextLine().split(" ");
        a = Integer.parseInt(s[0]);
        b = Integer.parseInt(s[1]);
        c = Integer.parseInt(s[2]);
        if(a + b == c){
            System.out.println("correct!");
        }
        else{
            System.out.println("wrong!");
        }
    }
}
