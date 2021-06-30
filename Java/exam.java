import java.util.Scanner;

public class exam {
    public static int notSame(int corrects, String F, String M){
        for(int i = 0; i < F.length(); i++){
            if(F.charAt(i) == M.charAt(i)){
                corrects --;
            }

        }

        return corrects;
    }

    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);
        int corrects = sc.nextInt();
        sc.nextLine();

        String friend = sc.nextLine();
        String me = sc.nextLine();

        int R = Math.abs(notSame(corrects, friend, me));

        System.out.println(me.length() - R);
    }
}
