import java.util.Scanner;

public class hangman{
    
    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);
        String word = sc.nextLine();
        String guess = sc.nextLine();
        int lives = 10;
        for(int i = 0; i < guess.length(); i++){
            if(word.length() == 0){
                break;
            }
            
            if(word.contains("" + guess.charAt(i))){
                word = word.replace("" + guess.charAt(i), "");
            }
            else{
                lives --;
            }
        }
    
        if(lives > 0){
            System.out.println("WIN");
        }
        else{
            System.out.println("LOSE");
        }
        
    }
}
