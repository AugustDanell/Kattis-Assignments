import java.util.Scanner;

/**
 * Created by August DH on 2016-12-17.
 */
public class SevenWonders {
    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);
        String input = sc.nextLine();

        int TCount = 0;
        int CCount = 0;
        int GCount = 0;
       // int SetOfThreeCount = 0;
        int totalCount = 0;

        for(int i = 0; i<input.length(); i++){
            if(input.charAt(i) == 'T'){
                TCount ++;
            }

            if(input.charAt(i) == 'C'){
                CCount ++;
            }

            if(input.charAt(i) == 'G'){
                GCount ++;
            }
        }

        totalCount += Math.pow(TCount, 2);
        totalCount += Math.pow(CCount, 2);
        totalCount += Math.pow(GCount, 2);

        while((TCount -1) >= 0 && (CCount -1) >= 0 && (GCount -1) >= 0){
            totalCount += 7;

            TCount --;
            CCount --;
            GCount --;
        }

        System.out.print(totalCount);
    }
}
