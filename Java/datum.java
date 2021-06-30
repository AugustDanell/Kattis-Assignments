import java.util.Scanner;

/**
 * Created by August DH on 2017-04-08.
 */
public class datum {
    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);
        String input = sc.nextLine();
        String[] splitted = input.split(" ");

        int searchedForDay = Integer.parseInt(splitted[0]);
        int searchedForMonth = Integer.parseInt(splitted[1]);



        int day = 3;    //Starts on thursday, 0 is monday.
        int currentMonth = 1;  //Starts in January.
        int dayOfTheMonth = 1;

        while (dayOfTheMonth != searchedForDay || currentMonth != searchedForMonth){
            dayOfTheMonth ++;
            day ++;
            day %= 7;

            if(dayOfTheMonth == 32 && (currentMonth == 1 || currentMonth == 3 || currentMonth == 5 || currentMonth == 7 || currentMonth == 8 || currentMonth == 10 || currentMonth == 12)){
                currentMonth ++;
                dayOfTheMonth = 1;
            }
            else if(dayOfTheMonth == 31 && (currentMonth == 4 || currentMonth == 6 || currentMonth == 9 || currentMonth == 11)){
                currentMonth ++;
                dayOfTheMonth = 1;
            }
            else if (dayOfTheMonth == 29 && currentMonth == 2){ //The February case
                currentMonth ++;
                dayOfTheMonth = 1;
            }
        }
        switch (day){
            case 0: System.out.println("Monday");
            break;

            case 1: System.out.println("Tuesday");
            break;

            case 2: System.out.println("Wednesday");
            break;

            case 3: System.out.println("Thursday");
            break;

            case 4: System.out.println("Friday");
            break;

            case 5: System.out.println("Saturday");
            break;

            case 6: System.out.println("Sunday");
            break;
        }

        //System.out.print(day);
    }
}
