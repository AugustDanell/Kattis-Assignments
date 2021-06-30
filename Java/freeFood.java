import java.util.ArrayList;
import java.util.Scanner;

public class freeFood {
    public static ArrayList list = new ArrayList<Integer>();
    public static int count = 0;

    public static void insertion(int a, int b){
        while(a <= b){
            if(!list.contains(a)){
                count ++;
                list.add(a);
            }

            a++;
        }
    }

    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);
        int cases = sc.nextInt();
        sc.nextLine();  // Flush

        for(int i = 0; i < cases; i++){
            String inp = sc.nextLine();
            String[] split = inp.split(" ");

            insertion(Integer.parseInt(split[0]), Integer.parseInt(split[1]));
        }

        System.out.print(count);
    }
}
