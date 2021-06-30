import java.util.ArrayList;
import java.util.Scanner;

public class boatParts {
    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);
        String input = sc.nextLine();
        String[] split = input.split(" ");

        int n = Integer.parseInt(split[1]);
        int p = Integer.parseInt(split[0]);

        ArrayList<String> list = new ArrayList<String>();
        int dayCount = 1;

        for(int i = 0; i < n; i++){
            String inp = sc.nextLine();
            if(!list.contains(inp)){
                p --;
                list.add(inp);
            }
            if(p == 0){
                break;
            }

            dayCount ++;
        }

        if(p == 0){
            System.out.print(dayCount);
        }
        else{
            System.out.print("paradox avoided");
        }
    }
}
