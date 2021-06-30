import java.util.Scanner;

/**
 * Created by August DH on 2016-12-19.
 */
public class Prsteni {

    public int leastPrime(int primeCandidate){
        for(int i = 2; i < primeCandidate-1; i++){
            if(primeCandidate%i == 0){
                return i;
            }
        }
        return 2;
    }

    public static int greatestPrime(int primeCandidate){
        for(int i = primeCandidate -1; i > 1; i--){
            if(primeCandidate%i == 0){
                return i;
            }
        }
        return 2;
    }

    public static int gcd(int large, int small){
        int val = small-1;// Start value
        while(((large%val) != 0) || ((small % val) != 0)){
            val--;
           // System.out.println(val);
        }

        return val;
    }

    public static void main(String[]args){
        Prsteni test = new Prsteni();
        Scanner sc = new Scanner(System.in);
        int amountOfRings = sc.nextInt();
        sc.nextLine();
        StringBuilder builderBob = new StringBuilder();

        String input = sc.nextLine();
        String[] splittedInput = input.split(" ");
        int[] rings = new int[amountOfRings];

        for(int i = 0; i < rings.length; i++){
            rings[i] = Integer.parseInt(splittedInput[i]);
        }
        //We skip the first ring
        for(int i = 1; i < rings.length; i++) {
            if (rings[0] % rings[i] == 0) {
                builderBob.append((rings[0] / rings[i]) + "/1");
            }
            else if(rings[0] % rings[i] != 0){
                int a = rings[0];
                int b = rings[i];
                int gd = gcd(a, b); //4

               // System.out.println(a + "\t" + b + "\t" + gd);
                builderBob.append(a/gd + "/"+b/gd);
            }

            if(i != rings.length - 1){
                builderBob.append("\n");
            }
        }
        System.out.print(builderBob.toString());
    }
}
