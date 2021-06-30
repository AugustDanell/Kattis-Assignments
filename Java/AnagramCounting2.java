import java.math.BigInteger;
import java.util.Scanner;

/**
 * Created by August DH on 2017-02-19.
 */
public class AnagramCounting2 {
    public static BigInteger factorial(int factorand){
        BigInteger product = new BigInteger("1");

        for(int i = 1; i <= factorand; i++){
            BigInteger factor = new BigInteger("" + i);
            product = product.multiply(factor);
        }

        return product;
    }


    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);
        StringBuilder builder = new StringBuilder();

        while(sc.hasNextLine()){
            String usedLetters = "";
            String anagram = sc.nextLine();
            BigInteger anagramsDenominator = new BigInteger("1");

            for(int i = 0; i < anagram.length(); i++){
                if(!usedLetters.contains(("" + anagram.charAt(i))) || usedLetters.length() == 0){
                    usedLetters += "" + anagram.charAt(i) + " ";

                    int occurances = 1;
                    for(int j = 0; j < anagram.length(); j++){
                        if(j != i && anagram.charAt(i) == anagram.charAt(j)){
                            occurances ++;
                        }
                    }

                    anagramsDenominator = anagramsDenominator.multiply(factorial(occurances));
                }
            }


            BigInteger anagramsNominator = factorial(anagram.length());
            //System.out.print(anagramsNominator.divide(anagramsDenominator));
            builder.append(anagramsNominator.divide(anagramsDenominator) + "\n");

        }

        System.out.print(builder.toString());
    }
}
