import java.util.ArrayList;
import java.util.Scanner;

public class GCD {
    public static ArrayList<Integer> factorize(int n){
        int index = 2;
        ArrayList<Integer> factors = new ArrayList<>();

        while (n != 1){
            if(n%index == 0){
                n = n / index;
                factors.add(index);
                index = 2;
            }
            else{
                index ++;
            }
        }

        return factors;
    }

    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);
        String[] s = sc.nextLine().split(" ");

        ArrayList<Integer> factors = factorize(Integer.parseInt(s[0]));
        int product = 1;
        int b = Integer.parseInt(s[1]);

        for(int i = 0; i < factors.size(); i++){
            if(b%factors.get(i) == 0){
                b = b/factors.get(i);
                product *= factors.get(i);
            }
        }

        System.out.println(product);
    }
}
