import java.util.Scanner;

public class heirsDilemma {
    public static boolean checkUnique(int i){

        String ex = Integer.toString(i);
        String concatenatingString = "";
        boolean Unique = true;

        if(ex.contains("0")){
            return false;
        }

        for(int j = 0; j < ex.length(); j++){
            if(!concatenatingString.contains("" + ex.charAt(j))){
                concatenatingString += ex.charAt(j);
            }
            else{
                Unique = false;
                break;
            }
        }

        return Unique;
    }

    public static boolean checkDivisible(int i){
        String ex = Integer.toString(i);
        boolean divisible = true;

        for(int j = 0; j < ex.length(); j++){
            if(i % Integer.parseInt("" + ex.charAt(j)) != 0){
                divisible = false;
                break;
            }
        }

        return divisible;
    }

    public static int combinations(int x, int y){
        int sum = 0;
        for(int i = x; i <= y; i++){
            if(checkUnique(i) && checkDivisible(i)){
                sum ++;
            }
        }

        return sum;
    }

    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);
        String input = sc.nextLine();
        String[] split = input.split(" ");

        int x = Integer.parseInt(split[0]);
        int y = Integer.parseInt(split[1]);

        System.out.println(combinations(x, y));
    }
}
