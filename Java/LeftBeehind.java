import java.util.Scanner;

/**
 * Created by August DH on 2016-12-18.
 */
public class LeftBeehind {
    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);
        boolean run = true;
        StringBuilder builderBob = new StringBuilder();

        while(run){
            String input = sc.nextLine();
            String[] splittedInput = input.split(" ");

            int Sweet = Integer.parseInt(splittedInput[0]);
            int Sour = Integer.parseInt(splittedInput[1]);

            boolean numberThirteen = false;
            if((Sweet + Sour) == 13){
                numberThirteen = true;
            }

            if(Sweet == 0 && Sour == 0){
                run = false;
            }
            else {
                if(Sweet > Sour && !numberThirteen){
                    builderBob.append("To the convention." + "\n");
                }

                if(Sour > Sweet && !numberThirteen){
                    builderBob.append("Left beehind." + "\n");
                }

                if(numberThirteen){
                    builderBob.append("Never speak again." + "\n");
                }

                if(Sour == Sweet){
                    builderBob.append("Undecided." + "\n");
                }
            }
        }
        System.out.print(builderBob.toString());
    }
}
