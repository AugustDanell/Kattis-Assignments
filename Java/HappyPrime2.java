import java.util.ArrayList;
import java.util.Scanner;

/**
 * Created by August DH on 2017-08-13.
 * Solution to Happy Happy Prime Prime.
 */
public class HappyPrime2 {
    public static boolean checkPrime(int candidate){
        if(candidate == 1){
            return false;
        }

        int i = 2;
        while (i <= candidate/2){
            if(candidate%i == 0){
                return false;
            }
            i++;
        }
        return true;
    }

    public static boolean checkHappy(int candidate){
        //ArrayList<Integer> prevList = new ArrayList<>();

        while(candidate != 1){
            //Four becomes 7 -> 10 -> 1

            if(candidate == 2 || candidate == 3 || candidate == 4 ||candidate == 5 || candidate ==  6 || candidate == 8 || candidate == 9){
                break;
            }
            int sum = 0;
            String n = "" + candidate;

            for(int i = 0; i < n.length(); i++){
                sum += Math.pow(Integer.parseInt("" + n.charAt(i)), 2);
            }

            candidate = sum;
        }

        if(candidate == 1){
            return  true;
        }
        else{
            return false;
        }
    }

    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        sc.nextLine();

        for(int i = 0; i < N; i++){
            String input = sc.nextLine();
            String[] splitted = input.split(" ");

            int P = Integer.parseInt(splitted[1]);

            if(checkPrime(P) && checkHappy(P)){
                System.out.println(splitted[0] + " " + P + " YES");
            }
            else{
                System.out.println(splitted[0] + " " + P + " NO");
            }
        }
    }
}
