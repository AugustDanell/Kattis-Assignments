import java.util.Scanner;

public class krizaljka {
    public static int indexA = 0;
    public static int indexB = 0;

    public static void indexMatch(String a, String b){
        boolean match = false;

        for(int i = 0; i < a.length(); i++){
            if(match){
                break;
            }

            for(int j = 0; j < b.length(); j++){
                if(b.charAt(j) == a.charAt(i)){
                    indexA = j;
                    indexB = i;
                    match = true;
                    break;
                }
            }
        }
    }

    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);
        String input = sc.nextLine();
        String[] split = input.split(" ");

        String a = split[0];
        String b = split[1];

        indexMatch(a, b);

        // OK! System.out.println(indexA + " " + indexB);

        for(int i = 0; i < b.length(); i++){
            for(int j = 0; j < a.length(); j++){
                if(i == indexA){
                   System.out.print(a);
                   break;
                }
                else if(j == indexB){
                    System.out.print(b.charAt(i));
                }
                else {
                    System.out.print(".");
                }
            }

            if(i +1 != b.length()){
                System.out.println();
            }
        }
    }
}
