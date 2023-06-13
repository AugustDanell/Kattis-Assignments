import java.util.Scanner;

public class grading{
    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);
        String[] split = sc.nextLine().split(" ");
        boolean found = false;
        int score = sc.nextInt();
        for(int i = 0; i < split.length; i++){
            if(score >= Integer.parseInt(split[i])){
                System.out.println((char)(i+65));
                found = true;
                break;
            }
        }
        
        if(!found){
            System.out.println("F");
        }
    }
}
