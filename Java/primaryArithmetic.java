import java.util.Scanner;

public class primaryArithmetic {
    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);

        while(true){
            String input = sc.nextLine();
            if(input.equals("0 0")){
                break;
            }
            else{
                carryOperations(input);
            }
        }
    }
    public static void carryOperations(String input){
        String[] splitted = input.split(" ");
        int length = Math.min(splitted[0].length(), splitted[1].length());
        int carries = 0;

        boolean increment = false;
        int track = 0;

        //splitted[0] = rev(splitted[0]);
        //splitted[1] = rev(splitted[1]);



        for(int i = length-1; i >= 0; i--){
            int diffK = 0;
            int diffJ = 0;

            if(splitted[0].length() > splitted[1].length()){
                diffK = getDiff(splitted[0].length(), splitted[1].length());
            }
            else if(splitted[1].length() > splitted[0].length()){
                diffJ = getDiff(splitted[1].length(), splitted[0].length());
            }

            int k = Integer.parseInt("" + splitted[0].charAt(i + diffK));
            int j = Integer.parseInt("" + splitted[1].charAt(i + diffJ));

            //System.out.println("K: " + k + "\t" + "J: "+ j);

            if(increment){
                k ++;
                increment = false;
                //System.out.println("FALSE");
            }

            if(k+j > 9){
                //System.out.println("TRUE");
                carries ++;
                increment = true;
            }
            track ++;
            //System.out.println("TRACK: " + track);
        }

        //Check after addition has been completed
        if(increment){
            //If splitted[0] is larger:
            splitted[0] = rev(splitted[0]);
            while(track < splitted[0].length()){
                if(checkCarry(track, splitted[0])){
                    carries ++;
                }
                else{
                    break;
                }
                track ++;
            }

            //If splitted[1] is the larger one:
            splitted[1] = rev(splitted[1]);
            while(track < splitted[1].length()){
                if(checkCarry(track, splitted[1])){
                    carries ++;
                }
                else{
                    break;
                }
                track ++;
            }
        }

        //Printing options
        if(carries == 0){
            System.out.println("No carry operation.");
        }
        else if (carries == 1){
            System.out.println("1 carry operation.");
        }
        else{
            System.out.println(carries + " carry operations.");
        }
    }

    public static boolean checkCarry(int index, String input){
        //System.out.println(Integer.parseInt("" + input.charAt(index)) + 1);
        if(Integer.parseInt("" + input.charAt(index)) + 1 > 9){
            return true;
        }
        else{
            return false;
        }
    }

    public static String rev(String input){
        StringBuilder bob = new StringBuilder();
        for(int i = input.length() - 1; i >= 0; i--){
            bob.append(input.charAt(i));
        }

        //System.out.println(bob.toString());
        return bob.toString();
    }

    public static int getDiff(int i, int j){
        return i - j;
    }
}
