import java.util.Scanner;

public class unlockPattern {
    public static double getDistance(int x1, int y1, int x2, int y2){
    //Euclidean distance formula
        int xdiff = x1 - x2;
        int ydiff = y1 - y2;

        int diff = Math.abs(((xdiff)*xdiff) + ((ydiff)*ydiff));
        return Math.sqrt(diff);
    }

    public static void main(String[]args){
        int grid[][] = new int[3][3];
        int x = 0;
        int y = 0;
        boolean test = false; //Testing flag

        if(test)
        System.out.println(getDistance(1,2,0, 2)); //OK!
        double distance = 0;
        Scanner sc = new Scanner(System.in);

        // User input for the phone display.
        for(int i = 0; i < 3; i++){
            String keys = sc.nextLine();
            String[] split = keys.split(" ");

            int a = Integer.parseInt(split[0]);
            int b = Integer.parseInt(split[1]);
            int c = Integer.parseInt(split[2]);

            grid[i][0] = a;
            grid[i][1] = b;
            grid[i][2] = c;
        }

        //Now we find the position of element 1.
        for(int i = 0; i < 3; i++){
            for(int j = 0; j < 3; j++){
                if(grid[i][j] == 1){
                    x = i;
                    y = j;
                }
            }
        }

        // Now we iterate through the grid 8 times for the other elements.
        for(int k = 2; k <= 9; k++) {
            for (int i = 0; i < 3; i++) {
                for (int j = 0; j < 3; j++) {
                    if (grid[i][j] == k) {
                        //i and j become the new coordinates.
                        if(test) {
                            System.out.println(x + " " + y);
                            System.out.println(i + " " + j);
                            System.out.println();
                        }
                        distance += getDistance(x, y, i, j);

                        x = i;  // Old x becomes current x
                        y = j;  // Likewise with y
                    }
                }
            }
        }

        System.out.println(distance);
    }
}
