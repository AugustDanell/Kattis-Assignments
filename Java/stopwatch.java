import java.util.Scanner;

public class stopwatch{
    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);
        int takes = sc.nextInt();
        sc.nextLine();
        boolean start = false;
        int prev = 0;
        int time = 0;
        
        for(int i = 0; i < takes; i++){
            int take = sc.nextInt();
            sc.nextLine();
            start = !start;
            if(start){
                prev = take;
            }
            else{
                time += take - prev;
            }
        }
        
        if(takes%2 == 1){
            System.out.println("still running");
        }
        else{
            System.out.println(time);
        }
    }
}
