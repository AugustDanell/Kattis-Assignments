import java.util.Scanner;

/**
 * Created by August DH on 2017-07-10.
 */
public class Natcanje2 {
    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);
        String teamInput = sc.nextLine();
        String[] splitted = teamInput.split(" ");

        int N = Integer.parseInt(splitted[0]);
        int S = Integer.parseInt(splitted[1]);
        int R = Integer.parseInt(splitted[2]);

        boolean[] brokenArray = new boolean[N];
        for(int i = 0; i < N; i++){
            brokenArray[i] = false;
        }

        boolean[] reserveArray = new boolean[N];
        for(int i = 0; i < N; i++){
            reserveArray[i] = false;
        }

        String brokenKayaks = sc.nextLine();
        splitted = brokenKayaks.split(" ");

        //Initiates the array of broken kayaks
        for(int i = 0; i < splitted.length; i++){
            brokenArray[Integer.parseInt(splitted[i]) - 1] = true;
        }

        String reserveKayaks = sc.nextLine();
        splitted = reserveKayaks.split(" ");

        //Initiates the array of reserve kayaks
        for(int i = 0; i < splitted.length; i++){
            reserveArray[Integer.parseInt(splitted[i]) - 1] = true;
        }

        int kayaksUnableToEnter = 0;
        //The kayak algortihm
        //Left FIRST
        for(int i = 0; i < N; i++){
            if(brokenArray[i]){
                boolean haveBoat = false;
                if(reserveArray[i]){
                    reserveArray[i] = false;
                    haveBoat = true;
                }
                else if(i!= 0 && reserveArray[i-1]){
                    //Avoiding out of bounds exception.
                    reserveArray[i-1] = false;
                    haveBoat = true;
                }
                else if(i != N-1 && reserveArray[i+1]){

                    reserveArray[i+1] = false;
                    haveBoat = true;
                }
                if(!haveBoat){
                    kayaksUnableToEnter ++;
                }
            }

        }

        System.out.print(kayaksUnableToEnter);
    }
}
