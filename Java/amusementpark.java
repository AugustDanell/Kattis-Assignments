import java.text.DecimalFormat;
import java.text.NumberFormat;
import java.util.*;

/**
 * Created by August DH on 2017-08-14.
 * Kattis Problem : Not Amused.
 */
public class amusementpark {
    public static ArrayList<String> sloppySort(HashMap<String, Integer> map){
        ArrayList<String> keys = new ArrayList<String>(map.keySet());
        Collections.sort(keys);

        return keys;
    }

    public static void sort(HashMap<String, Integer> map){
    }

    public static void printCustomerList(int day, HashMap<String, Integer> list, boolean first){
        String returnString = "Day " + day + "\n";
        ArrayList<String> keys = sloppySort(list);

        for(int i = 0; i < list.size(); i++){
            double fee = (double)list.get(keys.get(i));
            fee /= 10;

            NumberFormat formatter = new DecimalFormat("#0.00");

            returnString += (keys.get(i) + " $" + formatter.format(fee) + "\n");
            returnString = returnString.replace(",", ".");
        }

        System.out.println(returnString);
    }

    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);
        int day = 1;
        boolean first = true;

        HashMap<String, Integer> openList = new HashMap<>();
        HashMap<String, Integer> customerList = new HashMap<>();
        while (sc.hasNextLine()){
            String input = sc.nextLine();
            String[] splitted = input.split(" ");

            if(splitted[0].equals("ENTER")){
                openList.put(splitted[1], Integer.parseInt(splitted[2]));
            }
            else if(splitted[0].equals("EXIT")){
                int appendage = 0;
                if(customerList.containsKey(splitted[1])){
                    appendage = customerList.get(splitted[1]); //To copy the old value
                }

                customerList.put(splitted[1], (Integer.parseInt(splitted[2]) + appendage) - openList.get(splitted[1]));
            }
            else if(splitted[0].equals("CLOSE")){
                //Sorts the map.


                //Prints the map.
                printCustomerList(day, customerList, first);
                first = false;
                day ++;

                //Empties the maps.
                openList = new HashMap<>();
                customerList = new HashMap<>();
            }
        }
    }
}
