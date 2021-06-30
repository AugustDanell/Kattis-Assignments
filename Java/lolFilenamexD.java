import java.util.Scanner;

// För långt filnamn.
// Solution to : Greedily Increasing Subsequence
public class lolFilenamexD {

        public static void main(String[]args){
            Scanner sc = new Scanner(System.in);
            int numbers = sc.nextInt();
            sc.nextLine();
            StringBuilder bob = new StringBuilder();

            String input = sc.nextLine();
            String[] split = input.split(" ");
            int currentLargest = 0;
            int count = 0;

            for(int i = 0; i < numbers; i++){
                if(Integer.parseInt(split[i]) > currentLargest){
                    currentLargest = Integer.parseInt(split[i]);
                    bob.append(split[i]);
                    count ++;

                    if(i+1 != numbers){
                        bob.append(" ");
                    }
                }
            }

            System.out.println(count);
            System.out.print(bob.toString());
    }

}
