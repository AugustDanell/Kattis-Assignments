import java.util.Scanner;

/**
 * Created by August DH on 2017-09-02.
 */
public class mosquitoMultiplication {
    public static Scanner sc = new Scanner(System.in);
    public static void main(String[]args){
        while(sc.hasNextLine()){
            String input = sc.nextLine();
            Mos(input);
        }
    }

    public static void Mos(String input){
        String[] splitted = input.split(" ");
        int Mo = Integer.parseInt(splitted[0]);
        int Pu = Integer.parseInt(splitted[1]);
        int La = Integer.parseInt(splitted[2]);
        int Eggrate = Integer.parseInt(splitted[3]);
        int ToBePu = Integer.parseInt(splitted[4]);
        int ToBeMo = Integer.parseInt(splitted[5]);
        int time = Integer.parseInt(splitted[6]);
        int Eg = 0;

        for(int i = 0; i < time; i++){
            Eg = Mo * Eggrate; //Every mosquito lays e eggs and then dies a most grizzly death knowing that his day as a blood sucking, degenerate being is at an end!
            Mo = 0; //Prev Mos dies OK

            int tempLa = La/ToBePu;
            La = (Eg); // Move here - /ToBePu

            int tempPu = Pu/ToBeMo;
            Pu = (tempLa);

            Mo = tempPu;
        }

        System.out.println(Mo);
    }
}
