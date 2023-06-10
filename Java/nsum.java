import java.util.Scanner;

public class nsum{
    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        sc.nextLine(); //Flush
        
        int acc = 0;
        String[] s = sc.nextLine().split(" ");
        for(int i = 0; i < N; i++){
            acc += Integer.parseInt(s[i]);
        }
        System.out.println(acc);
    }
}
