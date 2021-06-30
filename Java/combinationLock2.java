import java.util.Scanner;

/**
 * Created by August DH on 2017-08-06.
 */
public class combinationLock2 {
    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);

        boolean run = true;
        StringBuilder builder = new StringBuilder();

        while(run){
            String input = sc.nextLine();
            if(input.equals("0 0 0 0")){
                run = false;
            }
            else{
                String[] splitted = input.split(" ");
                int degrees = 360 * 3; // All the turns are accounted for in advance.
                int position = Integer.parseInt(splitted[0]); //Start pos

                int firstComb = Integer.parseInt(splitted[1]);
                int secondComb = Integer.parseInt(splitted[2]);
                int thirdComb = Integer.parseInt(splitted[3]);

                //First combination - Clockwise
                    degrees += (9*(position - firstComb) + 360)%360;
                    position = firstComb;
                    //System.out.println(degrees);

                //Second combination - Counter clockwise
                    degrees += (9*(secondComb - position) + 360)%360;
                    position = secondComb;
                    //System.out.println(degrees);

                //Third combination - Clockwise again
                    degrees += (9*(position - thirdComb) + 360)%360;
                    position = thirdComb;
                    //System.out.println(degrees);

                    builder.append(degrees +"\n");
            }
        }

        System.out.print(builder.toString());
    }
}
