import java.util.Scanner;

/**
 * Created by August DH on 2017-02-05.
 */
public class quiteAProblem {
    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);
        StringBuilder builder = new StringBuilder();

        while(sc.hasNextLine()){
            String input = sc.nextLine();
            boolean found = false;

            for(int i = 0; i < input.length() - 6; i++) {
                String segment = input.substring(i, i+7);
                //System.out.println(segment);
                if (segment.matches("((P|p)(R|r)(O|o)(B|b)(L|l)(E|e)(M|m))")) {
                  //  System.out.println("19");
                    builder.append("yes" + "\n");
                    found = true;
                    break;
                }
            }

            if(!found){
                builder.append("no" + "\n");
            }
        }

        System.out.print(builder.toString());
    }
}

