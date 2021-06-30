import java.util.Scanner;

public class babyBites {
    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);
        int numbers = sc.nextInt();
        sc.nextLine();

        String inputMumblings = sc.nextLine();
        String[] split = inputMumblings.split(" ");
        boolean fishy = false;

        for(int i = 0; i < numbers; i++){
            if(!(split[i].equals("" + (i+1)) || split[i].equals("mumble"))){
                fishy = true;
                break;
            }
        }

        if(fishy){
            System.out.print("something is fishy");
        }
        else{
            System.out.print("makes sense");
        }
    }
}
