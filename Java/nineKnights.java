import java.util.Scanner;

public class nineKnights {
    public static boolean nineKnights(String[] board){
        int nineKnights = 0;

        for(int i = 0; i < 5; i++){
            for(int j = 0; j < 5; j++){
                if(board[i].charAt(j) == 'k'){
                    nineKnights ++;
                }
            }
        }

        if(nineKnights == 9){
            return true;
        }
        else{
            return false;
        }
    }

    public static boolean check(String[] board, int r, int c){
        boolean validMove = true;

        if(board[r].charAt(c) == '.'){
            return validMove;
        }
        else{   //Check all the moves
            if(c+2 <= 4 && r-1 >= 0 && board[r-1].charAt(c+2) == 'k'){
                validMove = false;
            }

            if(c+2 <= 4 && r+1 <= 4 && board[r+1].charAt(c+2) == 'k'){
                validMove = false;
            }

            if(c-2 >= 0 && r-1 >= 0 && board[r-1].charAt(c-2) == 'k'){
                validMove = false;
            }

            if(c-2 >= 0 && r+1 <= 4 && board[r+1].charAt(c-2) == 'k'){
                validMove = false;
            }
            // Row checks
            if(c-1 >= 0 && r-2 >= 0 && board[r-2].charAt(c-1) == 'k'){
                validMove = false;
            }

            if(c+1 <= 4 && r-2 >= 0 && board[r-2].charAt(c+1) == 'k'){
                validMove = false;
            }

            if(c-1 >= 0 && r+2 <= 4 && board[r+2].charAt(c-1) == 'k'){
                validMove = false;
            }

            if(c+1 <= 4 && r+2 <= 4 && board[r+2].charAt(c+1) == 'k'){
                validMove = false;
            }
        }

        return validMove;
    }

    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);
        String[] board = new String[5];
        boolean valid = true;

        for(int i = 0; i < 5; i++){
            board[i] = sc.nextLine();
        }

        for(int i = 0; i < 5; i++){
            if(!valid){
                break;
            }

            for(int j = 0; j < 5; j++){
                if(!check(board, i, j) || !nineKnights(board)){
                    valid = false;
                    break;
                }
            }
        }

        if(valid){
            System.out.println("valid");
        }
        else{
            System.out.println("invalid");
        }
    }
}
