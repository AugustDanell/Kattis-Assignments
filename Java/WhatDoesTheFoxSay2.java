import java.util.ArrayList;
import java.util.Scanner;

/**
 * Created by August DH on 2017-06-26.
 */
public class WhatDoesTheFoxSay2 {
    public static void main(String[]args){
        Scanner sc = new Scanner (System.in);
        int tests = sc.nextInt();
        sc.nextLine();
        StringBuilder builder = new StringBuilder();

        for(int i = 0; i < tests; i ++){
            String AllSound = sc.nextLine();
            String[] splittedSound = AllSound.split(" ");

            boolean run = true;
            ArrayList<String> soundList = new ArrayList<>();
            while(run){
                String sound = sc.nextLine();
                if(sound.equals("what does the fox say?")){
                    run = false;
                    String Answer = "";
                    for(int j = 0; j < splittedSound.length; j++){
                        if(!soundList.contains(splittedSound[j])){
                            builder.append(splittedSound[j] + " ");
                        }
                    }
                    builder.append("\n");

                }
                else{
                    String[] splittedIndividualSound = sound.split(" ");
                    soundList.add(splittedIndividualSound[splittedIndividualSound.length-1]);
                }
            }
        }

        System.out.print(builder.toString());
    }
}
