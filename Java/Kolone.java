import java.util.Scanner;

/**
 * Created by August DH on 2017-02-04.
 */
public class Kolone {
    public static class Ant{
        boolean goingRight;
        char antId;

        public Ant(char id, boolean right){
            antId = id;
            goingRight = right;
        }

        public boolean getDirection(){
            return goingRight;
        }

        public char getId(){
            return antId;
        }
    }

    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);
        String rows = sc.nextLine();
        String[] splittedRows = rows.split(" ");

        int NumberOfAntsInRowA = Integer.parseInt(splittedRows[0]);
        int NumberOfAntsInRowB = Integer.parseInt(splittedRows[1]);

        Ant[] allAnts = new Ant[NumberOfAntsInRowA + NumberOfAntsInRowB];

        String reversedRowA = sc.nextLine();
        //Ant[] rightAnts = new Ant[NumberOfAntsInRowA];

        for(int i = 0; i < reversedRowA.length(); i++){
            Ant rightAnt = new Ant(reversedRowA.charAt(reversedRowA.length()-i -1), true);
            allAnts[i] = rightAnt;
        }

        String rowB = sc.nextLine();
        Ant[] leftAnts = new Ant[NumberOfAntsInRowB];
        for(int i = NumberOfAntsInRowA; i < (NumberOfAntsInRowB + NumberOfAntsInRowA); i++){
            Ant leftAnt = new Ant(rowB.charAt(i-NumberOfAntsInRowA), false);
            allAnts[i] = leftAnt;
        }

        //Ovanstående kod funkar.
        /*
        for(int i = 0; i < (NumberOfAntsInRowA + NumberOfAntsInRowB); i++){
            //System.out.print(rightAnts[i].antId);
            //System.out.print(leftAnts[i].antId);
            //System.out.print(allAnts[i].antId);
        }
        */
        int seconds = sc.nextInt();
        sc.nextLine();

        //Varje myra i olika riktning byter plats för varje sekund
        for(int i = 0; i < seconds; i++){
            boolean dontMove = false;
            for(int j = 0; j < allAnts.length-1; j++){
                //If the ants are going in different directions, swap.
                if(allAnts[j].goingRight && !allAnts[j+1].goingRight && !dontMove){
                    Ant Temp = allAnts[j];
                    allAnts[j] = allAnts[j+1];
                    allAnts[j+1] = Temp;
                    dontMove = true;
                }
                else{
                    //Så att man inte gör flera "hopp" samma veva
                    dontMove = false;
                }
            }
        }




        for(int i = 0; i < (NumberOfAntsInRowA + NumberOfAntsInRowB); i++){
            //System.out.print(rightAnts[i].antId);
            //System.out.print(leftAnts[i].antId);
            System.out.print(allAnts[i].antId);
        }
    }
}
