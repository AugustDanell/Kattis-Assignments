import java.util.Scanner;

/**
 * Created by August DH on 2017-03-02.
 */
public class zamka2 {
    public static int digitSum(int check){
        if(check < 10){
            return check;
        }
        else if(check < 100){
            return ((check/10) + (check%10));
        }
        else if(check < 1000){
            return ((check/100) + ((check/10)%10) + check%10);
        }
        else{
            if(check == 10000){
                return 1;
            }

            return ((check/1000) + ((check/100)%10) + ((check/10)%10) + check%10);
        }
    }

    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);
        int L = sc.nextInt();
        sc.nextLine();

        int D = sc.nextInt();
        sc.nextLine();

        int X = sc.nextInt();
        sc.nextLine();

        int lower = L;
        int higher = D;

        for(int i = 0; i < D; i++){
            if(digitSum(lower) == X){
                break;
            }
            else{
                lower++;
            }
        }

        for(int i = 0; i < D; i++){
            if(digitSum(higher) == X){
                break;
            }
            else{
                higher--;
            }
        }

        System.out.println(lower + "\n" + higher);
        //Testing the method
        //System.out.println(digitSum(12));
    }
}
