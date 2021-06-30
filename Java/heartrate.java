import java.util.Scanner;

public class heartrate {
    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);
        int cases = sc.nextInt();
        sc.nextLine();

        StringBuilder bob = new StringBuilder();

        for(int i = 0; i < cases; i++){
            String inp = sc.nextLine();
            String[] split = inp.split(" ");

            int b = Integer.parseInt(split[0]);
            double p = Double.parseDouble(split[1]);

            double BPM = (double)(60*b)/p;
            double BPMminusONE = (double)(60*(b-1))/p;
            double BPMplusONE = (double)(60*(b+1))/p;

            bob.append(BPMminusONE + " " + BPM + " " + BPMplusONE + "\n");
        }

        System.out.print(bob.toString());
    }
}
