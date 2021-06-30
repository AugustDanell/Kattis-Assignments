import java.util.Scanner;

/**
 * Created by August DH on 2017-03-30.
 */
public class Semafori2 {
    private static class lightPost{
        //Starts with red
        int redDuration;
        int greenDuration;

        lightPost(int red, int green){
            redDuration = red;
            greenDuration = green;
        }

        public boolean checkIfGreen(int duration){
            boolean isGreen = false;
            while(duration > 0){
                if(!isGreen){
                    duration -= redDuration;
                }
                else{
                    duration -= greenDuration;
                }

                if(duration >= 0) {
                    isGreen = !isGreen;
                }
            }

            return isGreen;
        }

    }

    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);
        String input = sc.nextLine();
        String[] splitted = input.split(" ");

        int N = Integer.parseInt(splitted[0]); // Number of lights.
        int L = Integer.parseInt(splitted[1]); // Length of road.

        //Creation of lampposts
        lightPost arrayOfPosts[] = new lightPost[L];
        for(int i = 0; i < N; i++){
            String lightInput = sc.nextLine();
            String[] splittedLightInput = lightInput.split(" ");

            int D = Integer.parseInt(splittedLightInput[0]);
            int R = Integer.parseInt(splittedLightInput[1]);
            int G = Integer.parseInt(splittedLightInput[2]);

            lightPost newLightPost = new lightPost(R, G);
            arrayOfPosts[D] = newLightPost;
        }

        //The driving phase
        int distance = 0;
        int time = 0;
        while(distance != L){
            if(arrayOfPosts[distance] != null){
                if(arrayOfPosts[distance].checkIfGreen(time)){
                    distance++;
                }
                //else do not increment distance
            }
            else{
                distance ++;
            }

            time ++;
        }

        System.out.print(time);
    }
}
