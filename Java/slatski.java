import java.util.Scanner;

public class slatski {
    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);
        String input = sc.nextLine();
        String[] splitted = input.split(" ");

        int zeros = Integer.parseInt(splitted[1]);
        int amount = Integer.parseInt(splitted[0]);
        int bill = generate(zeros);
        //System.out.println(bill);
        round(amount, bill);
    }
    public static int generate(int zeros){
        String returnString = "1";
        for(int i = 0; i < zeros; i++){
            returnString += "0";
        }

        return Integer.parseInt(returnString);
    }

    public static void round(int amount, int bill){
      int rest = amount % bill;
      if(rest >= (bill+1)/2){
          System.out.println(amount + (bill - rest));
      }
      else{
          System.out.println(amount - (rest));
      }
    }
}
