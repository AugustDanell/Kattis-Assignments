import java.util.Scanner;

/**
 * Created by August DH on 2017-03-08.
 */
public class weakVertices2 {
    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);
        StringBuilder builderBob = new StringBuilder();

        boolean run = true;
        while(run){
            int vertices = sc.nextInt();
            sc.nextLine();

            if(vertices == -1){
                run = false;
            }
            else{
                //Drawing up the matrix graph
                String[] matrixgraph = new String[vertices];
                for(int i = 0; i < vertices; i++){
                    String input = sc.nextLine();
                    String refinedInput = input.replaceAll(" ", "");
                    matrixgraph[i] = refinedInput;
                }

                for(int i = 0; i < matrixgraph.length; i++){

                    boolean isWeak = true;
                    for(int j = 0; j < matrixgraph[i].length(); j++){
                        //Could replace with matrixgraph.length because it will always be a nxn matrix
                        int connected = Integer.parseInt("" + matrixgraph[i].charAt(j));
                        if(connected == 1){
                            //Looking for additional connections
                            for(int k = 0; k < matrixgraph[j].length(); k++){
                                connected = Integer.parseInt("" + matrixgraph[i].charAt(k));
                                if(k != j && connected == 1){
                                    //If we are in here we must have two sets of connections to our vertex
                                    if(matrixgraph[j].charAt(k) == '1'){
                                        isWeak = false;
                                    }
                                }
                            }
                        }
                    }

                    if(isWeak){
                        builderBob.append(i + " ");
                    }
                }

                builderBob.append("\n");
            }
        }

        System.out.print(builderBob.toString());
    }
}
