import java.util.Scanner;

/**
 * Created by August DH on 2017-08-14.
 */
public class patulcji22 {
    public static void findReal(int sum, int[] block){
        for(int i = 0; i < 8; i++){
            for(int j = i+1; j < 9; j++){
                if(sum - block[j] - block[i] == 100){
                    for(int k = 0; k < 9; k++){
                        if(k != i && k != j){
                            System.out.print(block[k]);

                            if(k != 8){
                                System.out.println();
                            }
                        }
                    }
                }
            }
        }
    }

    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);
        int[] dwarves = new int[9];

        int sum = 0;
        for(int i = 0; i < 9; i++){
            int dwarf = sc.nextInt();
            sc.nextLine();

            sum += dwarf;
            dwarves[i] = dwarf;
        }

        findReal(sum, dwarves);
    }
}
