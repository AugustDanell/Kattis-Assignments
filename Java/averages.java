import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.Scanner;

/**
 * Created by August DH on 2017-03-07.
 * Kattis problem: Paradox with Averages
 */
public class averages {
    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);
        StringBuilder builder = new StringBuilder();

        int cases = sc.nextInt();
        sc.nextLine();

        for(int i = 0; i < cases; i++){
            ArrayList<Integer> computerList = new ArrayList<>();
            ArrayList<Integer> economicsList = new ArrayList<>();

            String blankspace = sc.nextLine();//For the blankspace preceding the test
            String students = sc.nextLine();

            String computerStudents = sc.nextLine();
            String[] splittedComputer = computerStudents.split(" ");

            double totalComputer = 0;
            for(int j = 0; j < splittedComputer.length; j++){
                totalComputer += Integer.parseInt(splittedComputer[j]);
                computerList.add(Integer.parseInt(splittedComputer[j]));
            }
            double averageComputerBefore = totalComputer/splittedComputer.length;

            String economicsStudents = sc.nextLine();
            String[] splittedEconomics = economicsStudents.split(" ");

            double totalEconomics = 0;
            for(int j = 0; j < splittedEconomics.length; j++){
                totalEconomics += Integer.parseInt(splittedEconomics[j]);
                economicsList.add(Integer.parseInt(splittedEconomics[j]));
            }

            double averageEconomicsBefore = totalEconomics/splittedEconomics.length;
            //Now we have the average iq for both institutions before the drop out.

            //Iterating through the computer students
            int funnyStudentSample = 0;
            for(int j = 0; j < computerList.size(); j++){
                if((totalComputer-computerList.get(j))/(computerList.size()-1) > averageComputerBefore
                   && (totalEconomics+computerList.get(j))/(economicsList.size()+1) > averageEconomicsBefore){
                    funnyStudentSample++;
                }
            }
            builder.append(funnyStudentSample + "\n");

        }
        System.out.print(builder.toString());
    }
}
