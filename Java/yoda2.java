import java.util.Scanner;

/**
 * Created by August DH on 2017-06-26.
 */
public class yoda2 {
    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);
        String A = sc.nextLine();
        String B = sc.nextLine();

        String One = "";
        String Two = "";

        boolean isOneYoda = true;
        boolean isTwoYoda = true;

        int index;



        if(A.length() > B.length()){
            index = A.length();
        }
        else{
            index= B.length();
        }

        //reversed strings of A and B respectively.
        String C = "";
        String D = "";

        for(int i = A.length()-1; i >= 0; i--){
            C += "" + A.charAt(i);
        }

        for(int i = B.length()-1; i >= 0; i--){
            D += "" + B.charAt(i);
        }

        for(int i = 0; i < index; i++){
            if(i+1 > C.length()){
                if(D.charAt(i) == '0'){
                    isOneYoda = false;
                    isTwoYoda = false;

                    One += "0";
                    Two += "0";
                }
                else{
                    isTwoYoda = false;

                    Two += "" + D.charAt(i);
                }
            }
            else if(i+1 > D.length()){
                if(C.charAt(i) == '0'){
                    isOneYoda = false;
                    isTwoYoda = false;

                    One += "0";
                    Two += "0";
                }
                else{
                    isOneYoda = false;

                    One += "" + C.charAt(i);
                }
            }
            else{
                //Here no string can be out of bounds.
                if((int) D.charAt(i) > (int) C.charAt(i)){
                    isTwoYoda = false;

                    Two += "" + D.charAt(i);
                }
                else if((int) C.charAt(i) > (int) D.charAt(i)){
                    isOneYoda = false;

                    One += "" + C.charAt(i);
                }
                else{
                    isOneYoda = false;
                    isTwoYoda = false;

                    One += "" + C.charAt(i);
                    Two += "" + D.charAt(i);
                }
            }
        }

        //Reversing back
        One = new StringBuilder(One).reverse().toString();
        Two = new StringBuilder(Two).reverse().toString();

        //Printing out the answers acquired
        if(isOneYoda){
            System.out.println("YODA");
        }
        else{
            System.out.println(Integer.parseInt(One));
        }

        if(isTwoYoda){
            System.out.println("YODA");
        }
        else{
            System.out.println(Integer.parseInt(Two));
        }
    }
}
