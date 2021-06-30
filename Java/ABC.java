import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

/**
 * Created by August DH on 2017-02-03.
 */
public class ABC {
    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);
        StringBuilder builder = new StringBuilder();
        ArrayList<Integer> sortingList = new ArrayList<>();


        for(int i = 0; i < 2; i++) {
            String input = sc.nextLine();

            //Declaring the ints to be parsed
            int integerOne = 0;
            int integerTwo = 0;
            int integerThree = 0;

            int integerA = 0;
            int integerB = 0;
            int integerC = 0;
            if(i == 0) {
                //System.out.println("Test");
                String[] splittedInput = input.split(" ");

                 integerOne = Integer.parseInt(splittedInput[0]);
                 integerTwo = Integer.parseInt(splittedInput[1]);
                 integerThree = Integer.parseInt(splittedInput[2]);

                 //System.out.print(integerOne);

                 sortingList.add(integerOne);
                 sortingList.add(integerTwo);
                 sortingList.add(integerThree);

            }
            else{
                //System.out.println(sortingList);
                Collections.sort(sortingList);


                    //Appending the ABC variables into the builder
                    String ABCInput = input;
                    for(int j = 0; j < 3; j++){
                        if(ABCInput.charAt(j) == 'A'){
                            builder.append(sortingList.get(0) + " ");
                        }

                        if(ABCInput.charAt(j) == 'B'){
                            builder.append(sortingList.get(1) + " ");
                        }

                        if(ABCInput.charAt(j) == 'C'){
                            builder.append(sortingList.get(2) + " ");
                        }
                    }
                }


            }

        System.out.println(builder.toString());
    }
}
