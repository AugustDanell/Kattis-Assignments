import java.util.Scanner;

/**
 * Created by August DH on 2017-06-26.
 */
public class Okviri2 {
    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);
        String input = sc.nextLine();
        StringBuilder builderBob = new StringBuilder();

        int row = 1;
        int length = 4*input.length() + 1;

        int counter = 1;
        //Row 1
        while(row == 1) {
            if(counter == 1) {
                builderBob.append("..#..");
            }
            else{
                if(counter%3 != 0){
                    builderBob.append(".#..");
                }
                else{
                    builderBob.append(".*..");
                }
            }


            if(counter == input.length()){
                row ++;
            }
            counter ++;
        }
        builderBob.append("\n");
        // End of Row One - Seems to work!

        //Beginning of Row Two!
        counter = 1;
        while(row == 2){
            if(counter == 1){
                builderBob.append(".#.#.");
            }
            else{
                if(counter %3 != 0){
                    builderBob.append("#.#.");
                }
                else{
                    builderBob.append("*.*.");
                }
            }

            if(counter == input.length()){
                row ++;
            }

            counter ++;
        }
        builderBob.append("\n");
        // End of Row One - Seems to work!

        //Beginning of Row Three
        counter = 1;
        while(row == 3){
            if(counter == 1){
                builderBob.append("#." + input.charAt(counter - 1) + ".");
            }
            else{
                if((counter -1)%3 == 0 && counter%3 != 0){
                    builderBob.append("*." + input.charAt(counter-1) + ".");
                }
                else if(counter%3 != 0){
                    builderBob.append("#." + input.charAt(counter-1) + ".");
                }
                else{
                    builderBob.append("*." + input.charAt(counter-1) + ".");
                }
            }
            if(counter == input.length()){
                row ++;
                //Last appendage
                if(counter%3 != 0){
                    builderBob.append("#");
                }
                else{
                    builderBob.append("*");
                }
            }

            counter ++;
        }
        //End of row 3
        builderBob.append("\n");
        //Beginning of Row 4 - Which is a duplicate of row 2
        counter = 1;
        while(row == 4){
            if(counter == 1){
                builderBob.append(".#.#.");
            }
            else{
                if(counter %3 != 0){
                    builderBob.append("#.#.");
                }
                else{
                    builderBob.append("*.*.");
                }
            }

            if(counter == input.length()){
                row ++;
            }

            counter ++;
        }
        builderBob.append("\n");
        //End of row 4

        //Beginning of Row 5 - Which is a duplicate of row 1.
        counter = 1;
        while(row == 5) {
            if(counter == 1) {
                builderBob.append("..#..");
            }
            else{
                if(counter%3 != 0){
                    builderBob.append(".#..");
                }
                else{
                    builderBob.append(".*..");
                }
            }


            if(counter == input.length()){
                row ++;
            }
            counter ++;
        }
        builderBob.append("\n");
        // End of Row five

        System.out.print(builderBob.toString());
    }
}
