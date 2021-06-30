import java.util.Scanner;

/**
 * Created by August DH on 2017-08-24.
 */
public class primaryRegister {
    public static boolean blownUp = false;
    public static int operations = 0;
    public static int v2, v3, v5, v7, v11, v13, v17, v19;

    public static void Rtwo(){
        v2 ++;
        v2 %= 2;
        operations ++;

        if(v2 == 0){
            Rthree();
        }

    }

    public static void Rthree(){
        v3 ++;
        v3 %= 3;
//        operations ++;

        if(v3 == 0){
            Rfive();
        }
        else{
            Rtwo();
        }
    }

    public static void Rfive(){
        v5 ++;
        v5 %= 5;
//        operations ++;

        if(v5 == 0){
            Rseven();
        }
        else{
            Rtwo();
        }
    }

    public static void Rseven(){
        v7 ++;
        v7 %= 7;
//        operations ++;

        if(v7 == 0){
            Releven();
        }
        else{
            Rtwo();
        }
    }

    public static void Releven(){
        v11 ++;
        v11 %= 11;
//        operations ++;

        if(v11 == 0){
            Rthirteen();
        }
        else{
            Rtwo();
        }
    }

    public static void Rthirteen(){
        v13 ++;
        v13 %= 13;
//        operations ++;

        if(v13 == 0){
            Rseventeen();
        }
        else{
            Rtwo();
        }
    }

    public static void Rseventeen(){
        v17 ++;
        v17 %= 17;
//        operations ++;

        if(v17 == 0){
            Rnineteen();
        }
        else{
            Rtwo();
        }
    }

    public static void Rnineteen(){
        v19 ++;
        v19 %= 19;
        //operations ++;

        if(v19 == 0){
            blownUp = true;
        }
        else{
            Rtwo();
        }
    }

    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);
        String input = sc.nextLine();
        String[] splitted = input.split(" ");

        int two = Integer.parseInt(splitted[0]);
        v2 = two;

        int three = Integer.parseInt(splitted[1]);
        v3 = three;

        int five = Integer.parseInt(splitted[2]);
        v5 = five;

        int seven = Integer.parseInt(splitted[3]);
        v7 = seven;

        int eleven = Integer.parseInt(splitted[4]);
        v11 = eleven;

        int thirteen = Integer.parseInt(splitted[5]);
        v13 = thirteen;

        int seventeen = Integer.parseInt(splitted[6]);
        v17 = seventeen;

        int nineteen = Integer.parseInt(splitted[7]);
        v19 = nineteen;

        while(!blownUp) {
            Rtwo();
        }
        
        /* The while loop above was used as to avoid Stack Overflow by calling the lowest level itteratively. As such the
        *  levels of recursion is not as high and does not exceed the memory that was allocated, and as such avoids the Stack Overflow.
        */
        System.out.print(operations - 1);
    }
}
