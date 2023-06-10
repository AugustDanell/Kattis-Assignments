import java.util.Scanner;
public class betting{
    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);
        float a = (sc.nextFloat()/100);
        float b = 1.0f - a; 
        System.out.println(1.0f/a);
        System.out.println(1.0f/b);
    }
}
