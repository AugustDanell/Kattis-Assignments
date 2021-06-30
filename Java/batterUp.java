import java.util.Scanner;

public class batterUp {
    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);
        int numbers = sc.nextInt();
        sc.nextLine();

        String input = sc.nextLine();
        int times = 0;
        double percentage = 0;

        String[] splitted = input.split(" ");
        for(int i = 0; i < splitted.length; i++){
            if(!splitted[i].equals("-1")){
                times ++;
                percentage += Double.parseDouble(splitted[i]);
            }
        }

        System.out.println(percentage/times);
    }
}
