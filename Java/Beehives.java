import java.util.ArrayList;
import java.util.Scanner;

/**
 * Created by August DH on 2017-02-19.
 */
public class Beehives {
    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);
        StringBuilder builder = new StringBuilder();

        boolean run = true;

        while(run) {
            String input = sc.nextLine();
            String[] splitted = input.split(" ");

            float d = Float.parseFloat(splitted[0]);
            int n = Integer.parseInt(splitted[1]);

            if(d == 0.0 && n == 0){
                run = false;
            }
            else{
                int sour = 0; int sweet = 0;

                ArrayList<Float> xCoordinates = new ArrayList<>();
                ArrayList<Float> yCoordinates = new ArrayList<>();
                for(int i = 0; i < n; i++){
                    String coordinates = sc.nextLine();
                    String[] splittedCoordinates = coordinates.split(" ");

                    float x = Float.parseFloat(splittedCoordinates[0]);
                    float y = Float.parseFloat(splittedCoordinates[1]);

                    xCoordinates.add(x);
                    yCoordinates.add(y);
                }

                //Checking for distance
                for(int i = 0; i < n; i++){
                    boolean isSour = false;
                    double distance = 0;
                    for(int j = 0; j < n; j++){
                        if(i != j) {
                            // sqrroot((x2 - x1)^2 + (y2 - y1)^2)).
                            distance = Math.sqrt(Math.pow(xCoordinates.get(i) - xCoordinates.get(j), 2) +
                                       Math.pow(yCoordinates.get(i) - yCoordinates.get(j), 2));
                            if(distance < d){
                                isSour = true;
                            }
                        }
                    }

                    if(isSour){
                        sour ++;
                    }
                    else {
                        sweet ++;
                    }
                }
                builder.append(sour + " sour, " + sweet + " sweet\n");
            }

        }

        System.out.print(builder.toString());
    }
}
