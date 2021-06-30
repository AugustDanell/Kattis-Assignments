import java.util.Scanner;

public class cudoviste {
    public static int calcParkSpaces(int R, int C, String board[], int s){
        int counter = 0;
        for(int i = 0; i < R-1; i++){
            for(int j = 0; j < C-1; j++){
                // Border Control
                int cars = 0;
                if(i != R-1 && j != C-1){

                    if(board[i].charAt(j) == '#'){
                        cars = 10;  // Makes matching impossible
                    }

                    if(board[i+1].charAt(j) == '#'){
                        cars = 10;  // Makes matching impossible
                    }

                    if(board[i].charAt(j+1) == '#'){
                        cars = 10;  // Makes matching impossible
                    }

                    if(board[i+1].charAt(j+1) == '#'){
                        cars = 10;  // Makes matching impossible
                    }

                    if(board[i].charAt(j) == 'X'){
                        cars ++;  // A car to squash
                    }

                    if(board[i+1].charAt(j) == 'X'){
                        cars ++;  // A car to squash
                    }

                    if(board[i].charAt(j+1) == 'X'){
                        cars ++;  //  A car to squash
                    }

                    if(board[i+1].charAt(j+1) == 'X'){
                        cars ++;  //  A car to squash
                    }
                }

                if(cars == s){
                    counter ++;
                }
            }
        }

        return counter;
    }

    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);
        String input = sc.nextLine();
        String[] split = input.split(" ");

        int R = Integer.parseInt(split[0]);
        int C = Integer.parseInt(split[1]);
        String board[] = new String[R];

        for(int i = 0; i < R; i++){
            board[i] = sc.nextLine();
        }

        System.out.println(calcParkSpaces(R, C, board, 0));
        System.out.println(calcParkSpaces(R, C, board, 1));
        System.out.println(calcParkSpaces(R, C, board, 2));
        System.out.println(calcParkSpaces(R, C, board, 3));
        System.out.print(calcParkSpaces(R, C, board, 4));
    }
}
