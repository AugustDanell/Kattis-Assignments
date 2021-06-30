import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

/**
 * Created by August DH on 2017-08-03.
 */
public class busySchedule2 {
    public static int convert(String candidate){
        String splitted[] = candidate.split(":");
        int returnSum = 0;
        if(splitted[0].equals("12")){
            splitted[0] = "0";
        }
        returnSum += Integer.parseInt(splitted[0]) * 100;
        returnSum += Integer.parseInt(splitted[1]);

        return returnSum;
    }

    public static void sort(ArrayList<String> list){
        //An insertion sort, using the convert function to determine if a string is greater or not.
        for(int i = 1; i < list.size(); i++){
            int j = i-1;
            String key = list.get(i);
            int element = convert(list.get(i));

            while(j >= 0 && convert(list.get(j)) > element){
                list.set(j+1, list.get(j));
                j = j-1;
            }

            list.set(j+1, key);
        }
    }
    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);
        boolean run = true;

        StringBuilder builder = new StringBuilder();
        while(run){
            int schedules = sc.nextInt();
            sc.nextLine();
            if(schedules == 0){
                run = false;
            }
            else{
                ArrayList<String> AMList = new ArrayList<>();
                ArrayList<String> PMList = new ArrayList<>();

                for(int i = 0; i < schedules; i++) {
                    String schedule = sc.nextLine();
                    String[] splitted = schedule.split(" ");

                    if (splitted[1].equals("a.m.")) {
                        AMList.add(splitted[0]);
                    } else {
                        PMList.add(splitted[0]);
                    }
                }

                sort(AMList); //Collections.sort(AMList);
                sort(PMList); //Collections.sort(PMList);

               // System.out.print(AMList.toString());

                //-- Del två ---//

                //Sorting 12:00 first.
                while(AMList.size() > 0 && AMList.get(AMList.size()-1).equals("12:00")){
                    builder.append("12:00 a.m.\n");
                    AMList.remove(AMList.size()-1);
                }
                while(AMList.size() > 0){
                    builder.append(AMList.get(0) + " a.m.\n");
                    AMList.remove(0);
                }
                while (PMList.size() > 0 && PMList.get(PMList.size() - 1).equals("12:00")) {
                    builder.append(PMList.get(PMList.size()-1) + " p.m.\n");
                    PMList.remove(PMList.size()-1);
                }
                while(PMList.size() > 0){
                    builder.append(PMList.get(0) + " p.m.\n");
                    PMList.remove(0);
                }

                builder.append("\n"); //New line.
            }
        }
    System.out.print(builder.toString());

    }
}
