import java.util.ArrayList;
import java.util.Arrays;
import java.util.Scanner;
public class waterfall {
    public static void DFS(int n, int m, char[][]grid, ArrayList<ArrayList<Integer>> toVisit){
        while(toVisit.size() > 0){
            // 0. Extract the current value:
            ArrayList<Integer> currentNode = toVisit.remove(toVisit.size() - 1);
            int currentRow = currentNode.get(0);
            int currentCol = currentNode.get(1);
            if(currentRow == n-1){
                continue;
            }
            else{
                char down = grid[currentRow+1][currentCol];
                // 1. Handle water flowing down:
                if(down == 'O'){
                    grid[currentRow+1][currentCol] = '~';
                    ArrayList<Integer> nextNode = new ArrayList<>(Arrays.asList(currentRow+1, currentCol));
                    toVisit.add(nextNode);
                }
                // 2. Handle water flowing left / right:
                else if(down == '#' || down == '?'){
                    ArrayList<ArrayList<Integer>> nextNodes = new ArrayList<>();
                    ArrayList<Integer> rightNode = new ArrayList<>(Arrays.asList(currentRow, currentCol+1));
                    ArrayList<Integer> leftNode = new ArrayList<>(Arrays.asList(currentRow, currentCol-1));
                    nextNodes.add(rightNode);
                    nextNodes.add(leftNode);
                    for(ArrayList<Integer> nextNode : nextNodes){
                        int nextRow = nextNode.get(0);
                        int nextCol = nextNode.get(1);
                        if(nextCol >= 0 && nextCol < m && grid[nextRow][nextCol] == 'O'){
                            grid[nextRow][nextCol] = '~';
                            toVisit.add(nextNode);
                        }
                    }
                }
            }
        }

        // Print the waterfall-augmented grid:
        for(char[] charArr : grid){
            System.out.println(new String(charArr));
        }

    }

    public static void main(String[]args){
        // Input:
        Scanner sc = new Scanner(System.in);
        String inputs[] = sc.nextLine().split(" ");
        int n = Integer.parseInt(inputs[0]);
        int m = Integer.parseInt(inputs[1]);
        int k = Integer.parseInt(inputs[2]);
        String waterfalls[] = sc.nextLine().split(" ");
        
        // Add initial values to the toVisit stack:
        ArrayList<ArrayList<Integer>> toVisit = new ArrayList<ArrayList<Integer>>();
        for(int i = 0; i < k; i++){
            ArrayList<Integer> waterfall = new ArrayList<Integer>();
            waterfall.add(0);
            waterfall.add(Integer.parseInt(waterfalls[i]));
            toVisit.add(waterfall);
        }
        
        // Init the grid:
        char[][] grid = new char[n][m];
        for(int i = 0; i < n; i++){
            String row = sc.nextLine();
            for(int j = 0; j < m; j++){
                grid[i][j] = row.charAt(j);
            }
        }
    
        // For every row where there should have been waterfall, insert it:
        for(String waterfall : waterfalls){
            grid[0][Integer.parseInt(waterfall)] = '~';
        }

        // Call the DFS:
        DFS(n,m,grid,toVisit);

    }
    
}
