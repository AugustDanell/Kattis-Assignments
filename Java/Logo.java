import java.util.Scanner;

public class Logo {
    public static double x = 0;
    public static double y = 0;
    public static double deg = 0;

    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);
        int tests = sc.nextInt();
        sc.nextLine();

        for(int i = 0; i < tests; i++){
            x = 0;  //Sets the global variables for every test case.
            y = 0;
            deg = 90;

            int instructions = sc.nextInt();
            sc.nextLine();
            for(int j = 0; j < instructions; j++){
                String input = sc.nextLine();
                String[] splitted = input.split(" ");
                int val = Integer.parseInt(splitted[1]);

                if(splitted[0].equals("fd")){
                    fd(val);
                }
                else if(splitted[0].equals("lt")){
                    lt(val);
                }
                else if(splitted[0].equals("bk")){
                    bk(val);
                }
                else{
                    rt(val);
                }

                //System.out.println(y);
            }
            System.out.println(getDist());
        }
    }
    public static void fd(int val){
        x += Math.cos(Math.toRadians(deg)) * val;
        y += Math.sin(Math.toRadians(deg)) * val;
    }
    public static void lt(int val){
        deg += val;
    }
    public static void bk(int val){
        x -= Math.cos(Math.toRadians(deg)) * val;
        y -= Math.sin(Math.toRadians(deg)) * val;
    }
    public static void rt(int val){
        deg -= val;
    }
    public static int getDist(){
        double sum = Math.sqrt(Math.pow(x,2) + Math.pow(y,2));
        sum += 0.5;
        return (int) sum;
    }

}
