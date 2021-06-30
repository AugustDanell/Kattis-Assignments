import java.util.Scanner;

/**
 * Created by August DH on 2017-04-21.
 */
public class imperialMeasurement2 {
    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);

        String input = sc.nextLine();
        String[] splitted = input.split(" ");

        int startUnits = Integer.parseInt(splitted[0]);
        int startLevel = 0;
        int wantedLevel = 0;

        switch (splitted[1]) {
            case "th":
                startLevel = 1;
                break;

            case "thou":
                startLevel = 1;
                break;

            case "in":
                startLevel = 2;
                break;

            case "inch":
                startLevel = 2;
                break;
            case "ft":
                startLevel = 3;
                break;

            case "foot":
                startLevel = 3;
                break;
            case "yd":
                startLevel = 4;
                break;

            case "yard":
                startLevel = 4;
                break;

            case "ch":
                startLevel = 5;
                break;

            case "chain":
                startLevel = 5;
                break;

            case "fur":
                startLevel = 6;
                break;

            case "furlong":
                startLevel = 6;
                break;

            case "mi":
                startLevel = 7;
                break;

            case "mile":
                startLevel = 7;
                break;

            case "lea":
                startLevel = 8;
                break;

            case "league":
                startLevel = 8;
                break;
        }

        switch (splitted[3]) {
            case "th":
                wantedLevel = 1;
                break;

            case "thou":
                wantedLevel = 1;
                break;

            case "in":
                wantedLevel = 2;
                break;

            case "inch":
                wantedLevel = 2;
                break;
            case "ft":
                wantedLevel = 3;
                break;

            case "foot":
                wantedLevel = 3;
                break;
            case "yd":
                wantedLevel = 4;
                break;

            case "yard":
                wantedLevel = 4;
                break;

            case "ch":
                wantedLevel = 5;
                break;

            case "chain":
                wantedLevel = 5;
                break;

            case "fur":
                wantedLevel = 6;
                break;

            case "furlong":
                wantedLevel = 6;
                break;

            case "mi":
                wantedLevel = 7;
                break;

            case "mile":
                wantedLevel = 7;
                break;

            case "lea":
                wantedLevel = 8;
                break;

            case "league":
                wantedLevel = 8;
                break;
        }

        double sum = Double.parseDouble(splitted[0]);
        boolean increase = true;

        if (wantedLevel < startLevel){
            increase = false;
        }

        while (startLevel != wantedLevel){
            if(!increase){
                startLevel --;
            }

            int degOrIncFactor = 0;

            if(startLevel == 8){
                degOrIncFactor = 1;
            }
            else if(startLevel == 7){
                degOrIncFactor = 3;
            }
            else if (startLevel == 6){  //
                degOrIncFactor = 8;
            }
            else if (startLevel == 5){  //Furlong
                degOrIncFactor = 10;
            }
            else if (startLevel == 4){  //Chain
                degOrIncFactor = 22;
            }
            else if (startLevel == 3){  //Feet
                degOrIncFactor = 3;
            }
            else if (startLevel == 2){  //Inch
                degOrIncFactor = 12;
            }
            else if (startLevel == 1){  //Thou
                degOrIncFactor = 1000;
            }

            if(increase){
                startLevel ++;
            }

            if(increase){
                sum /= degOrIncFactor;
            }else{
                sum *= degOrIncFactor;
            }
        }
        System.out.print(sum);
    }
}
