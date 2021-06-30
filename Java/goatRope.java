import java.util.Scanner;

public class goatRope {
    public static int optimal(int z, int z1, int z2){
        if(z <= z1){
            return z1;
        }
        else if(z>=z2){
            return z2;
        }
        else{
            return z;
        }
    }

    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);
        String input = sc.nextLine();
        String[] split = input.split(" ");

        int x = Integer.parseInt(split[0]);
        int y = Integer.parseInt(split[1]);
        int x1 = Integer.parseInt(split[2]);
        int y1 = Integer.parseInt(split[3]);
        int x2 = Integer.parseInt(split[4]);
        int y2 = Integer.parseInt(split[5]);

        int xOpt = optimal(x, x1, x2);
        int yOpt = optimal(y, y1, y2);

        System.out.println((double)Math.sqrt(Math.pow((x - xOpt),2) + (Math.pow((y-yOpt), 2))));

    }
}
