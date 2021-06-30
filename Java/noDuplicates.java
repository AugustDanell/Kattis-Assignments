import java.util.ArrayList;
import java.util.Scanner;

public class noDuplicates {
    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);
        String input = sc.nextLine();

        ArrayList<String> words = new ArrayList<>();
        String[] splitted = input.split(" ");
        boolean found = false;

        for(int i = 0; i < splitted.length; i++){
            if(!words.contains(splitted[i])){
                words.add(splitted[i]);
            }
            else{
                System.out.println("no");
                found = true;
                break;
            }
        }

        if(!found){
            System.out.println("yes");
        }
    }
}
