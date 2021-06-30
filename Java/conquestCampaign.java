import java.util.Scanner;

public class conquestCampaign {
    public static boolean isOccupaid(int board[][], int R, int C){
        for(int i = 0; i < R; i++){
            for(int j = 0; j < C; j++){
                if(board[i][j] == 0){
                    return false;
                }
            }
        }

        return true;
    }

    public static int spread(int R, int C, int matrix[][]){
        int days = 1;
        while(!isOccupaid(matrix, R, C)) {
            for (int i = 0; i < R; i++) {
                for (int j = 0; j < C; j++) {
                    if (i != 0 && matrix[i - 1][j] == 1 && matrix[i][j] != 1) {
                        matrix[i][j] = 2;
                    }

                    if (j != 0 && matrix[i][j - 1] == 1 && matrix[i][j] != 1) {
                        matrix[i][j] = 2;
                    }

                    if (i != (R - 1) && matrix[i + 1][j] == 1 && matrix[i][j] != 1) {
                        matrix[i][j] = 2;
                    }

                    if (j != (C - 1) && matrix[i][j + 1] == 1&& matrix[i][j] != 1) {
                        matrix[i][j] = 2;
                    }
                }
            }

            // Set 2 to 1
            for(int i = 0; i < R; i++){
                for(int j = 0; j < C; j++){
                    if(matrix[i][j] == 2){
                        matrix[i][j] = 1;
                    }
                }
            }

            days ++;
        }
        return days;
    }

    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);
        String input = sc.nextLine();
        String[] split = input.split(" ");

        int R = Integer.parseInt(split[0]);
        int C = Integer.parseInt(split[1]);
        int N = Integer.parseInt(split[2]);

        int[][] board = new int[R][C];
        for(int i = 0; i < R; i++){
            for(int j = 0; j < C; j++){
                board[i][j] = 0;
            }
        }

        for(int i = 0; i < N; i++){
            input = sc.nextLine();
            split = input.split(" ");

            int x = Integer.parseInt(split[0]);
            int y = Integer.parseInt(split[1]);

            board[x-1][y-1] = 1;
        }

        System.out.print(spread(R, C, board));
    }
}
