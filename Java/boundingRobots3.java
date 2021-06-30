import java.util.Scanner;

/**
 * Created by August DH on 2017-06-19.
 */
public class boundingRobots3 {
    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);
        boolean run = true;
        StringBuilder builder = new StringBuilder();

        while(run){
            String Roominput = sc.nextLine();
            if(Roominput.equals("0 0")){
                run = false;
            }
            else{
                String[] splitted = Roominput.split(" ");
                int roomWidth = Integer.parseInt(splitted[0]);
                int roomHeight = Integer.parseInt(splitted[1]);

                int X = 0;
                int Y = 0;
                int xThinks = 0;
                int yThinks = 0;

                int steps = sc.nextInt();
                sc.nextLine();

                for(int i = 0; i < steps; i++){
                    String walkPath = sc.nextLine();
                    String[] splittedWalkPath = walkPath.split(" ");

                    if(splittedWalkPath[0].equals("r")){
                        xThinks += Integer.parseInt(splittedWalkPath[1]);
                        if(X + Integer.parseInt(splittedWalkPath[1]) >= roomWidth){
                            X = roomWidth - 1;
                        }
                        else{
                            X += Integer.parseInt(splittedWalkPath[1]);
                        }
                    }
                    else if(splittedWalkPath[0].equals("l")){
                        xThinks -= Integer.parseInt(splittedWalkPath[1]);
                        if(X - Integer.parseInt(splittedWalkPath[1]) <= 0){
                            X = 0;
                        }
                        else{
                            X -= Integer.parseInt(splittedWalkPath[1]);
                        }
                    }
                    else if(splittedWalkPath[0].equals("u")){
                        yThinks += Integer.parseInt(splittedWalkPath[1]);
                        if(Y + Integer.parseInt(splittedWalkPath[1]) >= roomHeight){
                            Y = roomHeight - 1;
                        }
                        else{
                            Y += Integer.parseInt(splittedWalkPath[1]);
                        }
                    }
                    else if(splittedWalkPath[0].equals("d")){
                        yThinks -= Integer.parseInt(splittedWalkPath[1]);
                        if(Y - Integer.parseInt(splittedWalkPath[1]) <= 0){
                            Y = 0;
                        }
                        else{
                            Y -= Integer.parseInt(splittedWalkPath[1]);
                        }
                    }
                }

                builder.append("Robot thinks " + xThinks + " " + yThinks + "\n");
                builder.append("Actually at " + X + " " + Y + "\n\n");
            }
        }

        System.out.print(builder.toString());
    }
}
