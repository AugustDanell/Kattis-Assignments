import java.util.Scanner;

/**
 * Created by August DH on 2016-12-13.
 */
public class Tri {
    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);
        String input = sc.nextLine();

        String[] splittedStrings = input.split(" ");
        int IntegerOne = Integer.parseInt(splittedStrings[0]);
        int IntegerTwo = Integer.parseInt(splittedStrings[1]);
        int IntegerThree = Integer.parseInt(splittedStrings[2]);

        //First we handle the cases where the first two somehoe equals the last
        if(IntegerOne+IntegerTwo == IntegerThree){
            System.out.print(IntegerOne + "+" + IntegerTwo + "=" + IntegerThree);
        }
        else if(IntegerOne-IntegerTwo == IntegerThree){
            System.out.print(IntegerOne + "-" + IntegerTwo + "=" + IntegerThree);
        }
        else if(IntegerOne * IntegerTwo == IntegerThree){
            System.out.print(IntegerOne + "*" + IntegerTwo + "=" + IntegerThree);
        }
        else if(IntegerOne/IntegerTwo == IntegerThree){
            System.out.print(IntegerOne + "/" + IntegerTwo + "=" + IntegerThree);
        }

        else if(IntegerTwo + IntegerThree == IntegerOne){
            System.out.print(IntegerOne + "=" + IntegerTwo + "+" + IntegerThree);
        }
        else if(IntegerTwo - IntegerThree == IntegerOne){
            System.out.print(IntegerOne + "=" + IntegerTwo + "-" + IntegerThree);
        }
        else if(IntegerTwo * IntegerThree == IntegerOne){
            System.out.print(IntegerOne + "=" + IntegerTwo + "*" + IntegerThree);
        }
        else if(IntegerTwo / IntegerThree == IntegerOne){
            System.out.print(IntegerOne + "=" + IntegerTwo + "/" + IntegerThree);
        }
    }
}
