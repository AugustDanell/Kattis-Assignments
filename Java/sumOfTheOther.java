import java.util.Scanner;

/**
 * Created by August DH on 2017-03-05.
 */
public class sumOfTheOther {
    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);
        StringBuilder builder = new StringBuilder();

        while(sc.hasNextLine()){
            String input = sc.nextLine();
            String[] splitted = input.split(" ");

            for(int i = 0; i < splitted.length; i++){
                int sum = 0;
                for(int j = 0; j < splitted.length; j++){
                    if(i != j){
                        sum += Integer.parseInt(splitted[j]);
                    }
                }
                if(Integer.parseInt(splitted[i]) == sum){
                    builder.append(sum + "\n");
                    break;
                }
            }
        }

        System.out.print(builder.toString());
    }
}
