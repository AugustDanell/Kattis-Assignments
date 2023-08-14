// 741th kattis. Problem here: https://open.kattis.com/problems/relatives

import java.util.HashMap;
import java.util.Scanner;

public class relatives{
    public static int get_div(int N){
        for(int i = 2; i <= Math.sqrt(N); i++){
            if(N%i == 0){
                return i;
            }
        }
        return -1;
    }


    public static HashMap get_divisors(int N){
        HashMap<Integer, Integer> divisors = new HashMap<>();
        while(true){
            int divisor = get_div(N);
            if(divisor == -1){
                divisors.put(N, 1);
                break;
            }
            N /= divisor;
            if(divisors.containsKey(divisor)){
                divisors.put(divisor, divisors.get(divisor)+1);
            }
            else{
                divisors.put(divisor, 1);
            }
        }
        return divisors;
    }

    public static int eulers_phi_function(int N, HashMap<Integer,Integer> divisors){
        double complements = 1;
        for(int divisor : divisors.keySet()){
            complements *= (1.0-1.0/divisor);
        }
        return (int)Math.round((complements)*N);
    }
    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);
        while(true){
            int N = Integer.parseInt(sc.nextLine());
            if(N == 0)
                break;
            
            HashMap N_divisors = get_divisors(N);
            System.out.println(eulers_phi_function(N, N_divisors));
        }
    } 
}
