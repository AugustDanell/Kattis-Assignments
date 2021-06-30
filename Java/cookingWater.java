import java.util.Scanner;

public class cookingWater {
    public static String totalInterval(String x, String y){
        String splitted[] = x.split(" ");
        int x1 = Integer.parseInt(splitted[0]);
        int x2 = Integer.parseInt(splitted[1]);

        splitted = y.split(" ");
        int y1 = Integer.parseInt(splitted[0]);
        int y2 = Integer.parseInt(splitted[1]);

        //System.out.println("X: " + x + " Y: " + y);

        if(x1 > y2){  //Unvalid value
            return "-1";
        }
        else if(x2 < y1){ //Unvalid value
            return "-1";
        }
        else if (y2 > x2){ //If one of the values
            if(x1 < y1){
                return y1 + " " + x2;  //Cross return
            }

            return x;
        }
        /*else if(x1 < y1){
            //if(y2 > )

            return x;
        }*/
        else{
            return y;
        }

    }

    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);
        int testCases = sc.nextInt();
        sc.nextLine();

        boolean gunillaHasPoint = true;
        String totalInterval = "0 1000";

        for(int i = 0; i < testCases; i++){
            String newInterval = sc.nextLine();
            totalInterval = totalInterval(totalInterval, newInterval);

            if(totalInterval.equals("-1")){
                System.out.print("edward is right");
                gunillaHasPoint = false;
                break;
            }

            //System.out.println(totalInterval);
        }

        if(gunillaHasPoint){
            System.out.println("gunilla has a point");
        }
    }
}
