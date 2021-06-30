import java.util.Scanner;

/**
 * Created by August DH on 2017-08-24.
 */
public class jackpot {
    public static long getLargestNominator(String[] arr){
        long largest = Long.parseLong(arr[0]);
        for(int i = 1; i < arr.length; i++){
            long val = Long.parseLong(arr[i]);
            if(val > largest){
                largest = val;  //Sets new max.
            }
        }

        return largest;
    }

    public static long getSpins(String input){
        String[] splitted = input.split(" ");
        long spins = 1;
        long N = getLargestNominator(splitted);

        int i = 0;
        while(1 != 0){
            if(N*spins > 1000000000){
                return -1;
            }

            if(i == splitted.length){
                break;
                //Reaches all way through thus returning a satisfactory answer.
            }

            if((N*spins)%Long.parseLong(splitted[i]) != 0){
                //Fails for given spin.
                //System.out.println((N*spins));
                spins ++;
                i = 0;
            }
            else{
                i++;
            }
        }
        return N*spins;
    }

    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);
        int machines = sc.nextInt();
        sc.nextLine();

        for(int i = 0; i < machines; i++){
            int wheels = sc.nextInt();
            sc.nextLine();

            String input = sc.nextLine();

            long val = getSpins(input);
            if(val == -1){
                System.out.println("More than a billion.");
            }
            else {
                System.out.println(val);
            }
        }
    }
}
