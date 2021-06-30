import java.util.Scanner;

/**
 * Created by August DH on 2017-02-19.
 * Solution to Beekeeper
 */
public class Akcija2 {
    //This is actually "Beekeeper" I named it wrongly

    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);
        StringBuilder builder = new StringBuilder();


        boolean run = true;
        while(run) {
            int cases = sc.nextInt();
            sc.nextLine();

            if(cases == 0){
                run = false;
            }
            else{
                String currentFavorite = "";
                int leadingPoints = 0;

                for(int i = 0; i < cases; i++){
                    int points = 0;
                    String input = sc.nextLine();
                    
                    if(currentFavorite.equals("")){
                        currentFavorite = input;
                    }
                    
                    for(int j = 0; j < input.length()-1; j++){
                        if((("" + input.charAt(j)).matches("[aeiouy]")) && input.charAt(j) == input.charAt(j+1)){
                            points ++;
                        }
                    }
                    if(points > leadingPoints){
                        leadingPoints = points;
                        currentFavorite = input;
                    }
                }

                builder.append(currentFavorite +"\n");
            }

        }
        System.out.print(builder.toString());
    }
}
