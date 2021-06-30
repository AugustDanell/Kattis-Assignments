import java.math.BigInteger;
import java.util.Scanner;

/**
 * Created by August DH on 2017-08-15.
 */
public class factStoneBenchMark {
    public static int x = 0;
    public static int iter = 0;

    public static void testIteration(){
        x ++;
        if(x == 500){
            iter ++;
            System.out.println(iter + " iterations!");
            x = 0;
        }
    }

    public static void test (BigInteger bit, BigInteger fac, int n){
        System.out.println("The bit: " + bit.toString());
        System.out.println("The faculty value: " + fac.toString());
        System.out.println("N! = " + n);
    }

    public static BigInteger faculty(int fac){
        /* This method failed for higher, inputed years. This is because if a year is high enough
         * the faculty will also be high, and if the faculty is high enough the amount of
         * recursive calls will overflood the stack memory, resulting in a stack overflow.
         * Also, an iterative method is in general faster than it's recursive counter part.
         */
        BigInteger facke = new BigInteger("" + fac);
        if(fac > 2)
        facke = facke.multiply(faculty(fac -1));

        return facke;
    }

    public static BigInteger itFac(int fac){
        BigInteger facke = new BigInteger("" + fac);
        while(fac > 2){
            fac --;
            facke = facke.multiply(new BigInteger("" + (fac)));
        }

        return  facke;
    }

    public static void comparison(int bits) {
        BigInteger help = new BigInteger("1");
        BigInteger bit = new BigInteger("2");
        bit = bit.pow(bits);
        bit = bit.subtract(help);

        int i = 1;


        //An attempt at optimizing - Using premature values.
        /* The premature values have been optained using the loop algorithm showed
         * below and with a reasonable start guess. By using the values optained, the
         * performance will surely be elevated.
         */
        boolean premade = false;
        //System.out.println(bits);

        if(bits == 1024){
            i = 170;
            premade = true;
        }
        else if(bits == 2048){
            i = 300;
            premade = true;
        }
        else if(bits == 4096){
            i = 536;
            premade = true;
        }
        else if(bits == 8192){
            i = 966;
            premade = true;
        }
        else if(bits == 16384){  //2080
            i = 1754;
            premade = true;
        }
        else if(bits == 32768){
            i = 3210;
            premade = true;
        }
        else if(bits == 65536){
            i = 5910;
            premade = true;
        }
        else if(bits == 131072){
            i = 10944;
            premade = true;
        }
        else if(bits == 262144){
            i = 20366;
            premade = true;
        }
        else if(bits == 524288){
            i = 38064;
            premade = true;
        }
        else if(bits == 1048576){
            i = 71421;
            premade = true;
        }
        else if(bits == 2097152){
            i = 134480;
            premade = true;
        }
        else if(bits == 4194304 ){
            i = 254016;
            premade = true;
        }



        while(!premade && itFac(i+1).compareTo(bit) <= 0){
            //testIteration(); - Method to help evaluate start guesses.
            i++;
        }

        //test(bit, faculty(i+1), i+1);
        System.out.println(i);

    }

    public static int calculateBitSize(int year){
        int start = 1960;
        int Bit = 2;

        while(start <= year){
            Bit *= 2;
            start += 10;
        }

        return Bit;
    }

    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);
        boolean run = true;

        while(run){
            int year = sc.nextInt();
            sc.nextLine();

            if(year == 0){
                run = false;
            }
            else{
                int bits = calculateBitSize(year);
                //System.out.println(bits);

                comparison(bits);

            }
        }
    }
}
