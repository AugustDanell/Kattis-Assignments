import java.util.Scanner;

/**
 * Created by August DH on 2016-12-09.
 */
public class LineThemUp {
    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);
        String names = sc.nextLine();
        String[] splittedNames = names.split(" ");
        int numberOfNames = Integer.parseInt(splittedNames[0]);
        String returnString = "";
        String[] variousNames = new String[numberOfNames];

        int[] isIncrease = new int[numberOfNames];
        boolean increase = false;
        boolean decrease = false;

        for(int i = 0; i < numberOfNames; i++){
            isIncrease[i] = 0;
        }

        for(int i = 0; i<numberOfNames; i++){
            String name = sc.nextLine();
            variousNames[i] = name;
        }

        for(int i = 0; i < variousNames.length-1; i++){
            int j = 0;
            while(j<variousNames[i].length() && j < variousNames[i+1].length()){
                if((((int)variousNames[i].charAt(j)) < (int)variousNames[i+1].charAt(j)) && isIncrease[i] != -1){
                    increase = true;
                    isIncrease[i] = 1;
                }
                if(((int)variousNames[i].charAt(j) > (int)variousNames[i+1].charAt(j)) && isIncrease[i] != 1){
                    decrease = true;
                    isIncrease[i] = -1;
                }


                j++;
            }
        }

        if(increase && !decrease){
            returnString = "INCREASING";
        }

        if(!increase && decrease){
            returnString = "DECREASING";
        }

        if(increase && decrease){
            returnString = "NEITHER";
        }

        System.out.print(returnString);
    }
}
