import java.util.Arrays;
import java.util.Scanner;

/**
 * Created by August DH on 2016-12-12.
 */
public class SymmetricOrder {
    public static void main(String[]args) {
        //Input of the number of names
        Scanner sc = new Scanner(System.in);
        boolean run = true;
        int set = 0;
        String returnString = "";

        while (run){
            set ++;
            //Inputs the number of names
            String numberOfNames = sc.nextLine();
            String[] splittedString = numberOfNames.split(" ");
            int names = Integer.parseInt(splittedString[0]);

            String[] nameList = new String[names];

            if(names != 0) {
                for (int i = 0; i < names; i++) {
                    nameList[i] = sc.nextLine();

                }
                boolean isUnevenArrayDone=false;
                boolean isArrayEven = false;
                //Checks if the list is even
                if (nameList.length %2 == 0){
                    isArrayEven = true;
                }

                //Divides the nameList into two parts
                String[] nameListPart1 = new String[nameList.length/2];
                String[] nameListPart2 = new String[nameList.length/2];

                if(isArrayEven) {
                    int balence = 0;
                    int balence2 = 0;

                    for (int i = 0; i < names; i++) {

                        //If the Array is even
                        if (i % 2 == 0) {
                            nameListPart1[i - balence] = nameList[i];
                            balence2++;
                        }
                        if (i % 2 == 1) {
                            nameListPart2[i - balence2] = nameList[i];
                            balence++;
                        }
                    }
                    returnString += ("SET " + set +"\n");
                    for (int i = 0; i < names / 2; i++) {
                        returnString += (nameListPart1[i] +"\n");
                    }
                    for (int i = 0; i < names / 2; i++) {
                        returnString +=(nameListPart2[nameListPart2.length - i - 1]) + "\n";
                    }
                }
                else {
                    if (!isUnevenArrayDone) {
                        String mid = nameList[nameList.length - 1];
                        String[] eveniziedList = new String[nameList.length - 1];

                        //Creates a list without the middle name
                        int evenizingBalence = 0;
                        for (int i = 0; i < nameList.length - 1; i++) {
                            if (nameList[i] != mid) {
                                eveniziedList[i] = nameList[i + evenizingBalence];
                            } else {
                                eveniziedList[i] = nameList[i + 1];
                                evenizingBalence++;
                            }
                        }

                        //System.out.println(Arrays.toString(eveniziedList));

                        int balence = 0;
                        int balence2 = 0;

                        for (int i = 0; i < names - 1; i++) {

                            if (i % 2 == 0) {
                                nameListPart1[i - balence] = eveniziedList[i];
                                balence2++;
                            }
                            if (i % 2 == 1) {
                                nameListPart2[i - balence2] = eveniziedList[i];
                                balence++;
                            }

                        }
                        //System.out.println(Arrays.toString(nameListPart1));
                        //System.out.println(Arrays.toString(nameListPart2));
                        //System.out.println(mid);

                        returnString += ("SET " +set +"\n");
                        for(int i = 0; i < names/2; i++){
                            returnString +=  (nameListPart1[i]) + "\n";
                        }
                        returnString += (mid)+ "\n";
                        for(int i = 0; i < names/2; i++){
                            returnString += (nameListPart2[nameListPart2.length-i-1])+"\n";
                        }
                        //System.out.println(returnString);
                        //System.out.println(returnString);

                        isUnevenArrayDone = true;
                    }
                }

            }
            else{
                run = false;
                System.out.println(returnString);
            }
        }
    }
}
