import java.util.Scanner;

/**
 * Created by August DH on 2016-12-10.
 */
public class Pet {
    public static void main(String[]args){
        String[] deltagare = new String[5];
        int[] sumation = new int[5];

        Scanner sc = new Scanner(System.in);
        deltagare[0] = sc.nextLine();
        deltagare[1] = sc.nextLine();
        deltagare[2] = sc.nextLine();
        deltagare[3] = sc.nextLine();
        deltagare[4] = sc.nextLine();

        for (int i = 0; i<5; i++) {
            sumation[i] = Integer.parseInt((deltagare[i].substring(0,1))) +
                          Integer.parseInt(deltagare[i].substring(2,3)) +
                          Integer.parseInt(deltagare[i].substring(4,5)) +
                          Integer.parseInt(deltagare[i].substring(6,7));
        }

        if(sumation[0] > sumation[1] && sumation[0] > sumation[2] && sumation[0] > sumation[3] && sumation[0] > sumation[4]){
            System.out.println("1 " + sumation[0]);
        }
        else if (sumation[1] > sumation[0] && sumation[1] > sumation[2] && sumation[1] > sumation[3] && sumation[1] > sumation[4]){
            System.out.println("2 " + sumation[1]);
        }
        else if (sumation[2] > sumation[0] && sumation[2] > sumation[1] && sumation[2] > sumation[3] && sumation[2] > sumation[4]){
            System.out.println("3 " + sumation[2]);
        }
        else if(sumation[3] > sumation[0] && sumation[3] > sumation[1] && sumation[3] > sumation[2] && sumation[3] > sumation[4]){
            System.out.println("4 " + sumation[3]);
        }
        else if(sumation[4] > sumation[0] && sumation[4] > sumation[1] && sumation[4] > sumation[2] && sumation[4] > sumation[3]){
            System.out.println("5 " + sumation[4]);
        }
    }
}
