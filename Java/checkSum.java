import java.util.Scanner;
// Kattis Problem : Luhn Check Sum.

public class checkSum {
    public static int twoDigitSum(int n){
        if(2*n < 10){
            return 2*n;
        }
        else{
            return (2*n) / 10 + (2*n)%10;
        }
    }

    public static int sumTest(String n){
        String len = new StringBuilder( n ).reverse().toString();
        int length = len.length();
        int sum = 0;

        for(int i = 0; i < length; i+= 2){
            if(i == length){
                break;
            }

            if(i != length -1){
                sum += twoDigitSum(Integer.parseInt("" + len.charAt(i+1)));
            }
            sum += Integer.parseInt("" + len.charAt(i));
        }

        return sum;
    }

    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);
        int cases = sc.nextInt();
        sc.nextLine();
        StringBuilder bob = new StringBuilder();

        for (int i = 0; i < cases; i++){
            String inp = sc.nextLine();
            //long n = Long.parseLong(inp);

            if(sumTest(inp) % 10 == 0){
                bob.append("PASS");
            }
            else{
                bob.append("FAIL");
            }
//            bob.append(sumTest(n));
            bob.append("\n");
        }

        System.out.print(bob.toString());
    }
}
