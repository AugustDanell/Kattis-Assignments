import java.util.Scanner;

public class helpPhdCandidate {
    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);
        int cases = sc.nextInt();
        sc.nextLine();
        StringBuilder bob = new StringBuilder();

        for(int i = 0; i < cases; i++){
            String input = sc.nextLine();
            String[] split = input.split("\\+");

            if(input.equals("P=NP")){
                //System.out.print("skipped");
                bob.append("skipped\n");
            }
            else {
                int a = Integer.parseInt(split[0]);
                int b = Integer.parseInt(split[1]);

                //System.out.println(a + b);
                bob.append(a+b+"\n");
            }
        }

        System.out.print(bob.toString());
    }
}
