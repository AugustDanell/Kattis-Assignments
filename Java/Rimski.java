/* https://open.kattis.com/problems/rimski
   We want to redistribute the roman alphabet to form the smallest value that we can.
   90 and up should already be distributed in their best form in regards to XC.

   1 If we have an L we can organize an X in front of it, but only if we have but ONE X.
   2 Likewise we can organize an I in front of an X or V.

   We should start with checking one, and if impossible go to 2.


 */

import java.util.Scanner;

public class Rimski {

    // Method handling etc: LXIII -> XLIII
    static String reorganizationOne(String input){
        int x = 0;
        int L = 0;
        int I = 0;

        for(int i = 0; i < input.length(); i++){
           if(input.charAt(i) == 'X'){
               x ++;
           }
           else if(input.charAt(i) == 'L'){
               L ++;
           }
           else{
               I ++;
           }
        }

        if(L == 1 && x == 1) {
            return "XL" + input.substring(2);
        }
        else if(I == 1 && x == 2 && L == 1){
            return "XLIX";
        }
        return input;
    }

    static String reorganizationTwo(String input){
        // No L or V possible in here
        if(input.equals("XI")){
            return "IX";
        }
        int length = input.length() - 2;
        int I = 0;
        for(int i = 0; i < input.length(); i++){
            if(input.charAt(i) == 'V' || input.charAt(i) == 'L'){
                return input; // abort
            }
            if(input.charAt(i) == 'I'){
                I++;
            }
        }

        if(I != 1){
            return input; //abort
        }

        return input.substring(0, length) + "IX";
    }

    static String reorganizationThree(String input){
        //X is allowed and so is L
        int I = 0;
        int V = 0;

        for (int i = 0; i < input.length(); i++){
            if(input.charAt(i) == 'I'){
                I ++;
            }
            if(input.charAt(i) == 'V'){
                V++;
            }
        }

        if(I != 1 || V == 0){
            return input; //abortion
        }
        int length = input.length() - 2;
        return input.substring(0, length) + "IV";
    }
    public static void main(String[]args){
      Scanner sc = new Scanner(System.in);
      String inputRoman = sc.nextLine();
      if(inputRoman.length() > 1) {
          inputRoman = reorganizationOne(inputRoman);
          inputRoman = reorganizationTwo(inputRoman);
          inputRoman = reorganizationThree(inputRoman);
      }
      System.out.println(inputRoman);

    }
}
