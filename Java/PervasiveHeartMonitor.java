import java.util.Scanner;

/**
 * Created by August DH on 2016-12-16.
 */
public class PervasiveHeartMonitor {
    public static boolean checkIfName(String candidate){
        String[] splitted = candidate.split(" ");
        int asciiValueFirst = (int)splitted[0].charAt(0);

        if(asciiValueFirst >= 48 && asciiValueFirst <= 57){
            return false;
        }
        else{
            return true;
        }
    }
    
    public static void main(String[]args){
        Scanner sc = new Scanner (System.in);
        StringBuilder builderBob = new StringBuilder();

        while(sc.hasNextLine()){
            String nameInput = sc.nextLine();
            String[] splitted = nameInput.split(" ");

            boolean nameFirstOccur;
            int asciiValueFirst = (int)splitted[0].charAt(0);

            if(asciiValueFirst >= 48 && asciiValueFirst <= 57){
                nameFirstOccur = false;
            }
            else{
                nameFirstOccur = true;
            }
            
            String name = "";
            int numbers = 0;
            float average = 0;
            
            //if(nameFirstOccur){
            //    name += splitted[0];
                for(int i = 0; i < splitted.length; i++){
                    if(checkIfName(splitted[i])){
                       name += splitted[i] + " ";
                    }
                    else{
                        numbers ++;
                        average += Float.parseFloat(splitted[i]);
                    }
                }
            //}

            average /= numbers;
            builderBob.append(average + " " + name + "\n");
        }

        System.out.print(builderBob.toString());
    }
}
