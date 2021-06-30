import java.util.Scanner;

/**
 * Created by August DH on 2017-06-19.
 */
public class savingforRetirement2 {
    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);
        String input = sc.nextLine();
        String[] splitted = input.split(" ");

        int B = Integer.parseInt(splitted[0]);
        int Br = Integer.parseInt(splitted[1]);
        int Bs = Integer.parseInt(splitted[2]);
        int A = Integer.parseInt(splitted[3]);
        int As = Integer.parseInt(splitted[4]);

        int Bobsaved = (Br - B) * Bs;
        int aliceSaved = 0;

        while(aliceSaved <= Bobsaved){
            aliceSaved += As;
            A ++;
        }

        System.out.println(A);
    }
}
