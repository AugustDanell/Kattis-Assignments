import java.util.HashMap;
import java.util.HashSet;
import java.util.Scanner;
public class doubleDigits {
    public static boolean sameDigits(int x, int y){
        int z = x*y;
        //System.out.println("test " + x + " " + y + " :");
        HashMap<Integer, Integer> singleMap = new HashMap<>();
        HashMap<Integer, Integer> prodMap = new HashMap<>();
        while(x > 0){
            int digit = x % 10;
            int frequency = singleMap.getOrDefault(digit, 0) + 1;
            singleMap.put(digit, frequency);
            x /= 10;
        }
        while(y > 0){
            int digit = y % 10;
            int frequency = singleMap.getOrDefault(digit, 0) + 1;
            singleMap.put(digit, frequency);
            y /= 10;
        }
        while(z > 0){
            int digit = z%10;
            int frequency = prodMap.getOrDefault(digit, 0) + 1;
            prodMap.put(digit, frequency);
            z /= 10;
        }

        //System.out.println(singleMap.toString());
        //System.out.println(prodMap.toString());

        for(int key : prodMap.keySet()){
            if(!singleMap.containsKey(key) || singleMap.get(key) != prodMap.get(key)){
                return false;
            }
        }

        for(int key : singleMap.keySet()){
            if(!prodMap.containsKey(key)){
                return false;
            }
        }

        return true;
    }

    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);
        String inputString[] = sc.nextLine().split(" ");
        int a = Integer.parseInt(inputString[0]);
        int b = Integer.parseInt(inputString[1]);
        
        int count = 0;
        StringBuilder answers = new StringBuilder();
        for(int x = a; x <= b; x++){
            for(int y = x; y <= b; y++){
                if(sameDigits(x, y)){
                    count += 1;
                    answers.append("x = " + x + ", y = " + y + ", xy = " + x*y + "\n");
                }
            }
        }

        System.out.println(count + " digit-preserving pair(s)");
        System.out.print(answers.toString());
    }
    
}
