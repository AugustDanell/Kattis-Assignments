import java.util.ArrayList;
import java.util.Scanner;

/**
 * Created by August DH on 2017-03-07.
 */
public class sortOfSorting {
    public static void twoCharSort(ArrayList<String> list){
        //Need to fix this sorting method
        for (int i = 1; i < list.size(); i++){

            for (int j = i; j > 0 && (int)list.get(j-1).charAt(0) >= (int)list.get(j).charAt(0); j--){
                boolean secondIsGreater = true; //If first greater, this always true

                if((int)list.get(j-1).charAt(0) == (int)list.get(j).charAt(0)){
                    if((int)list.get(j-1).charAt(1) <= (int)list.get(j).charAt(1)){
                        secondIsGreater = false;
                    }
                }

                if(secondIsGreater) {
                    String temp = list.get(j);
                    list.set(j, list.get(j-1));
                    list.set(j-1, temp);
                }
            }
        }
    }

    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);
        StringBuilder builder = new StringBuilder();

        boolean run = true;
        while(run){
            int cases = sc.nextInt();
            sc.nextLine();

            if(cases == 0){
                run = false;

            }
            else{
                //Adding names to the list
                ArrayList<String> nameList = new ArrayList<>();

                for(int i = 0; i < cases; i++) {
                    String name = sc.nextLine();
                    nameList.add(name);
                }

                twoCharSort(nameList);


                for(int i = 0; i < nameList.size(); i++){
                    builder.append(nameList.get(i) + "\n");
                }
                builder.append("\n");
            }
        }

        System.out.print(builder.toString());
    }
}
