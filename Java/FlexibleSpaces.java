import java.util.ArrayList;
import java.util.Arrays;
import java.util.Scanner;

/**
 * Created by August DH on 2016-12-23.
 */
public class FlexibleSpaces {
    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);
        String widthInput = sc.nextLine();
        String[] splittedWidthInput = widthInput.split(" ");
        StringBuilder builderBob = new StringBuilder();

        int totalWidth = Integer.parseInt(splittedWidthInput[0]);
        int numberOfPartitions = Integer.parseInt(splittedWidthInput[1]);
        int[] partitions = new int[numberOfPartitions];

        ArrayList<Integer> listOfAvailableWidths = new ArrayList<Integer>();

        String spacesInput = sc.nextLine();
        String[] splittedSpacesInput = spacesInput.split(" ");


        int index = 0;
        for(int i = 0; i < totalWidth; i++){
            if (index < partitions.length && i == Integer.parseInt(splittedSpacesInput[index])) {
                partitions[index] = Integer.parseInt(splittedSpacesInput[index]);
                index++;
            }

        }

        for(int i = 0; i < partitions.length; i++){
            if(!listOfAvailableWidths.contains(totalWidth)){
                listOfAvailableWidths.add(totalWidth);
            }
            if(!listOfAvailableWidths.contains(partitions[i])){
                listOfAvailableWidths.add(partitions[i]);
            }
            if(!listOfAvailableWidths.contains(totalWidth-partitions[i])){
                listOfAvailableWidths.add(totalWidth-partitions[i]);
            }
        }

        for(int i = partitions.length-1; i >= 0; i--){
            for(int j = i-1; j >= 0; j--){
                //System.out.println(partitions[i]-partitions[j]);
                if(!listOfAvailableWidths.contains(partitions[i]-partitions[j])){
                    listOfAvailableWidths.add(partitions[i]-partitions[j]);
                }
            }
        }

        for(int i = 1; i < listOfAvailableWidths.size(); i++){
            int x = listOfAvailableWidths.get(i);
            int j = i-1;
            while(j>=0 && listOfAvailableWidths.get(j) > x){
                listOfAvailableWidths.set(j+1, listOfAvailableWidths.get(j));
                j = j -1;
            }
            listOfAvailableWidths.set(j+1,x);
        }

        for(int i = 0; i < listOfAvailableWidths.size(); i++){
            builderBob.append(listOfAvailableWidths.get(i) + " ");
        }

        System.out.print(builderBob.toString());
    }
}
