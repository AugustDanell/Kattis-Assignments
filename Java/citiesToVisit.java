// A Solution to this problem: https://open.kattis.com/problems/tripplanning

/**
 * General Solution Idea:
 * Just create a datastructure for maintaining a bidirectional adjlist (Undirected).
 * From there, just step 1 -> 2 .. N -> 1.
 * For each timestep, append the index of the edge to a stringbuilder.
 * If, at any timestep, there is no path as the one above, break and print impossible.
 * Else, print the output of the stringbuilder. 
 */

import java.util.HashMap;
import java.util.Scanner;
public class citiesToVisit {
    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);
        HashMap<Integer,HashMap<Integer, Integer>> adjList = new HashMap<>();
        String[] input = sc.nextLine().split(" ");
        int n = Integer.parseInt(input[0]);
        int m = Integer.parseInt(input[1]);

        // 1. Create the adjlist:
        for(int i = 0; i < m; i++){
            input = sc.nextLine().split(" ");
            int from = Integer.parseInt(input[0]);
            int to = Integer.parseInt(input[1]);

            // Since the edges are bidirectional, we create an undirected adjList (meaning from -> to && to -> from):
            HashMap<Integer, Integer> innerFromHashMap = adjList.getOrDefault(from, new HashMap<Integer, Integer>());
            HashMap<Integer, Integer> innerToHashMap   = adjList.getOrDefault(to,   new HashMap<Integer, Integer>());
            innerFromHashMap.put(to, i+1);
            innerToHashMap.put(from, i+1);
            adjList.put(from, innerFromHashMap);
            adjList.put(to, innerToHashMap);
        }

        // 2. Use the adjlist to always traverse as was mentioned in the general solution idea.
        int currentCity = 1;
        StringBuilder tour = new StringBuilder();
        while(adjList.containsKey(currentCity) && adjList.get(currentCity).containsKey(currentCity+1)){
            tour.append(adjList.get(currentCity).get(currentCity+1) + "\n");
            currentCity += 1;
        }
        
        if(currentCity == n && adjList.containsKey(n) && adjList.get(n).containsKey(1)){
            tour.append(adjList.get(currentCity).get(1));    
            System.out.println(tour.toString());
        }
        else{
            System.out.println("impossible");
        }
    }
}
