/*   A Solution to the problem: https://open.kattis.com/problems/runningmom
*    General Solution: A "special" BFS where we pass a hashmap alongside the next node to visit, indicating the paths that this node has traversed.
*    
*/

import java.util.HashMap;
import java.util.Scanner;
import java.util.ArrayDeque;
import java.util.ArrayList;


public class flights {
    public static boolean BFS(HashMap<String, ArrayList<String>> flights, String start){
        ArrayDeque<ArrayList<Object>> to_visit = new ArrayDeque<>();
        HashMap<String, Boolean> visited = new HashMap<>();
        ArrayList<Object> start_arr = new ArrayList<>();
        start_arr.add(start);
        start_arr.add(visited);
        visited.put(start, true);
        to_visit.add(start_arr);
        
        while(to_visit.size() > 0){
            ArrayList<Object> current_package = (ArrayList) to_visit.pollFirst();
            String current_node = (String)current_package.remove(0);
            HashMap<String, Boolean> old_path = (HashMap)current_package.remove(0);

            boolean test = false;
            if(test){
                System.out.println("Current node: " + current_node);
                for(String city: old_path.keySet()){
                    System.out.println("visited: " + city);
                }
                System.out.println("--------------------------------------------");
            }
            
            if(flights.containsKey(current_node)){
                for(int i = 0; i < flights.get(current_node).size(); i++){
                    HashMap<String, Boolean> current_path = new HashMap<>();
                    for(String visited_node: old_path.keySet()){
                        current_path.put(visited_node, true);
                    }
                    
                    String next_flight = flights.get(current_node).get(i);
                    if(current_path.containsKey(next_flight)){
                        return true;
                    }
                    else{
                        current_path.put(next_flight, true);
                        ArrayList<Object> next_package = new ArrayList<>();
                        next_package.add(next_flight);
                        next_package.add(current_path);
                        to_visit.add(next_package);
                    }
                }
            }            
        }   
        
        return false;
    }

    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);
        int cities = Integer.parseInt(sc.nextLine());
        HashMap<String, ArrayList<String>> flights = new HashMap<>();
        for(int i = 0; i < cities; i++){
            String[] split = sc.nextLine().split(" ");
            if(!flights.containsKey(split[0])){
                flights.put(split[0], new ArrayList<>());    
            }
            flights.get(split[0]).add(split[1]);
        }

        // READ TO EOF SIGNAL for when querying:
        while(sc.hasNextLine()){
            String query_city = sc.nextLine();
            if(BFS(flights, query_city)){
                System.out.println(query_city + " " + "safe");
            }
            else{
                System.out.println(query_city + " " + "trapped");
            }            
        }
    }    
}
