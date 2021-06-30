import java.util.Scanner;

/**
 * Created by August DH on 2017-08-27.
 */
public class flowLayout {
    public static void rectangles(int maxWidth){
        boolean runRectangles = true;
        Scanner sc = new Scanner(System.in);

        int largestWidth = 0;
        int largestHeight = 0;
        int largestRowHeight = 0;

        int currentWidth = 0;
        int rowIncrement = 0;

        while (runRectangles){
            String input = sc.nextLine();

            if(input.equals("-1 -1")){
                runRectangles = false;
            }
            else{
                String splitted[] = input.split(" ");
                int boxHeight = Integer.parseInt(splitted[1]);
                int boxWidth = Integer.parseInt(splitted[0]);

                currentWidth += boxWidth;
                if(currentWidth > maxWidth){
                    //New row
                    rowIncrement += largestRowHeight;

                    currentWidth = boxWidth;
                    largestRowHeight = boxHeight;

                }

                if(currentWidth > largestWidth){
                    largestWidth = currentWidth;
                }

                //Verkar fungera med width.

                if(largestRowHeight < boxHeight){
                    largestRowHeight = boxHeight;
                }

                if(largestHeight < boxHeight + rowIncrement){
                    largestHeight = boxHeight + rowIncrement;
                }
            }
        }

        System.out.println(largestWidth + " x " + largestHeight);
    }

    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);
        boolean run = true;

        while(run){
            int m = sc.nextInt();
            sc.nextLine();

            if(m == 0){
                run = false;
            }
            else{
                //rectangles(m);
                boolean runRectangles = true;
                //Scanner sc = new Scanner(System.in);

                int largestWidth = 0;
                int largestHeight = 0;
                int largestRowHeight = 0;

                int currentWidth = 0;
                int rowIncrement = 0;

                while (runRectangles){
                    String input = sc.nextLine();

                    if(input.equals("-1 -1")){
                        runRectangles = false;
                    }
                    else{
                        String splitted[] = input.split(" ");
                        int boxHeight = Integer.parseInt(splitted[1]);
                        int boxWidth = Integer.parseInt(splitted[0]);

                        currentWidth += boxWidth;
                        if(currentWidth > m){
                            //New row
                            rowIncrement += largestRowHeight;

                            currentWidth = boxWidth;
                            largestRowHeight = boxHeight;

                        }

                        if(currentWidth > largestWidth){
                            largestWidth = currentWidth;
                        }

                        //Verkar fungera med width.

                        if(largestRowHeight < boxHeight){
                            largestRowHeight = boxHeight;
                        }

                        if(largestHeight < boxHeight + rowIncrement){
                            largestHeight = boxHeight + rowIncrement;
                        }
                    }
                }

                System.out.println(largestWidth + " x " + largestHeight);

            }
        }
    }
}
