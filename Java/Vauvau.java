import java.util.Scanner;

/**
 * Created by August DH on 2016-12-14.
 */
public class Vauvau {
    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);
        String dogInput = sc.nextLine();
        String[] splittedInput = dogInput.split(" ");
        int timerA = 0;
        int timerB = 0;

        int dogAAttacksGarbageMan = 0;
        int dogBAttacksGarbageMan = 0;
        int dogAAttacksMailMan = 0;
        int dogBAttacksMailMan = 0;
        int dogAAttacksPostMan = 0;
        int dogBAttacksPostMan = 0;

        int dog1AggressiveTime = Integer.parseInt(splittedInput[0]);
        int dog1CalmTime = Integer.parseInt(splittedInput[1]);
        int dog2AggressiveTime = Integer.parseInt(splittedInput[2]);
        int dog2CalmTime = Integer.parseInt(splittedInput[3]);

        String visitInput = sc.nextLine();
        String[] splittedVisitInput = visitInput.split(" ");

        int postman = Integer.parseInt(splittedVisitInput[0]);
        int mailman = Integer.parseInt(splittedVisitInput[1]);
        int garbageman = Integer.parseInt(splittedVisitInput[2]);

        boolean DogAAggressive = true;
        boolean DogACalm = false;

        boolean DogBAggressive = true;
        boolean DogBCalm = false;

        for (int i = 0; i < 10000; i++){
            int aggresiveTime = 0;
            while(DogAAggressive){
                aggresiveTime ++;
                aggresiveTime = aggresiveTime%(dog1AggressiveTime);
                //System.out.println(aggresiveTime);
                if(aggresiveTime == 0){
                    DogAAggressive = false;
                    DogACalm = true;
                    //timerA--;
                }
                timerA++;


            if((timerA == postman) && (dogAAttacksPostMan != -1)){
                dogAAttacksPostMan = 1;
            }
            if((timerA == garbageman) && (dogAAttacksGarbageMan != -1)){
                dogAAttacksGarbageMan = 1;
            }
            if((timerA == mailman )&& (dogAAttacksMailMan != -1)){
                dogAAttacksMailMan = 1;
            }
        }

        int calmTime = 0;
            while (DogACalm) {
                calmTime++;
                calmTime = calmTime % (dog1CalmTime);
                //System.out.println(calmTime);
                if (calmTime == 0) {
                    DogAAggressive = true;
                    DogACalm = false;
                    //timerA--;
                }

                timerA++;


                if ((timerA == postman) && (dogAAttacksPostMan != 1)) {
                    dogAAttacksPostMan = -1;
                }
                if ((timerA == garbageman) && (dogAAttacksGarbageMan != 1)) {
                    dogAAttacksGarbageMan = -1;
                }
                if ((timerA == mailman) && (dogAAttacksMailMan != 1)) {
                    dogAAttacksMailMan = -1;
                }
            }

            int aggresiveTime2 = 0;
            while (DogBAggressive) {
                aggresiveTime2++;
                aggresiveTime2 = aggresiveTime2 % (dog2AggressiveTime);
                if (aggresiveTime2 == 0) {
                    DogBAggressive = false;
                    DogBCalm = true;
                    //timerB--;
                }
                timerB++;


                if ((timerB == postman) && (dogBAttacksPostMan != -1)) {
                    dogBAttacksPostMan = 1;
                }
                if ((timerB == garbageman) && (dogBAttacksGarbageMan != -1)) {
                    dogBAttacksGarbageMan = 1;
                }
                if ((timerB == mailman) && (dogBAttacksMailMan != -1)) {
                    dogBAttacksMailMan = 1;
                }
            }

            int calmTime2 = 0;
            while(DogBCalm){
                calmTime2 ++;
                calmTime2 = calmTime2%(dog2CalmTime);
                if(calmTime2 == 0){
                    DogBAggressive = true;
                    DogBCalm = false;
                    //timerB --;
                }

                timerB++;


                if((timerB == postman) && (dogBAttacksPostMan != 1)){
                    dogBAttacksPostMan = -1;
                }
                if((timerB == garbageman) && (dogBAttacksGarbageMan != 1)){
                    dogBAttacksGarbageMan = -1;
                }
                if((timerB == mailman) && (dogBAttacksMailMan != 1)){
                    dogBAttacksMailMan = -1;
                }
            }
        }

        String returnString = "";
        //String concatations which aims to print the return string for the program
        //POSTMAN
        if((dogAAttacksPostMan == 1 && dogBAttacksPostMan == -1)||(dogBAttacksPostMan == 1 && dogAAttacksPostMan == -1)){
            returnString += "one" + "\n";
        }
        if(dogAAttacksPostMan == 1 && dogBAttacksPostMan == 1){
            returnString += "both" + "\n";
        }
        if(dogAAttacksPostMan == -1 && dogBAttacksPostMan == -1){
            returnString += "none" + "\n";
        }

        //MAILMAN
        if((dogAAttacksMailMan == 1 && dogBAttacksMailMan == -1)||((dogAAttacksMailMan == -1) && dogBAttacksMailMan == 1 )){
            returnString +="one" + "\n";
        }
        if(dogAAttacksMailMan == 1 && dogBAttacksMailMan == 1){
            returnString +="both" + "\n";
        }
        if(dogAAttacksMailMan == -1 && dogBAttacksMailMan == -1){
            returnString += "none" + "\n";
        }
        //GARBAGEMAN
        if((dogAAttacksGarbageMan == 1 && dogBAttacksGarbageMan == -1) || (dogBAttacksGarbageMan == 1 && dogAAttacksGarbageMan == -1)){
            returnString += "one";
        }
        if(dogAAttacksGarbageMan == 1 && dogBAttacksGarbageMan == 1){
            returnString += "both";
        }
        if(dogAAttacksGarbageMan == -1 && dogBAttacksGarbageMan == -1){
            returnString += "none";
        }

        System.out.print(returnString);
    }
}
