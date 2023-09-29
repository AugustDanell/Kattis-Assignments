import java.util.ArrayList;
import java.util.Arrays;
import java.util.Scanner;
public class cypherDecypher {
    public static int charToNum(char chr){
        return ((int)chr) -65;
    }
    public static char numToChar(int num){
        return (char)(num + 65);
    }

    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);
        ArrayList<Integer> scalars = new ArrayList<>();
        String[] input = sc.nextLine().split("");
        for(String data : input){
            scalars.add(Integer.parseInt(data));
        }
        int n = Integer.parseInt(sc.nextLine());
        for(int i = 0; i < n; i++){
            String msg = sc.nextLine();
            char[] chrArr = new char[msg.length()];
            for(int j = 0; j < msg.length(); j++){
                int num = (charToNum(msg.charAt(j))*scalars.get(j))%26;
                chrArr[j] = numToChar(num);
            }
            System.out.println(new String(chrArr));
        }
    }
}
