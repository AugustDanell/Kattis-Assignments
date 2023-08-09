// 740th Kattis, link to problem here: https://open.kattis.com/problems/torn2pieces

import java.util.ArrayList;
import java.util.HashMap;
import java.util.Scanner;
import java.util.ArrayDeque;
import java.util.LinkedHashMap;

public class torn2pieces {
    public static String BFS(String start, String end, LinkedHashMap<String, LinkedHashMap<String, Boolean>> adj_list){
        ArrayDeque<LinkedHashMap<String, LinkedHashMap<String, Boolean>>> to_visit = new ArrayDeque<>();
        LinkedHashMap<String, LinkedHashMap<String, Boolean>> outer_hashmap = new LinkedHashMap<>();
        LinkedHashMap<String, Boolean> inner_HashMap = new LinkedHashMap<>();
        inner_HashMap.put(start, true);
        outer_hashmap.put(start, inner_HashMap);
        to_visit.add(outer_hashmap);
        //System.out.println(adj_list.toString());
        while(to_visit.size() > 0){
            LinkedHashMap<String, LinkedHashMap<String, Boolean>> current_package = to_visit.pollFirst();
            //System.out.println(current_package.toString());
            String current_node = (String)current_package.keySet().toArray()[0];
            LinkedHashMap<String, Boolean> visited = current_package.get(current_node);

            if(current_node.equals(end)){
                StringBuilder SB = new StringBuilder();
                for(String key : visited.keySet()){
                    SB.append(key);
                    SB.append(" ");
                }
                SB.deleteCharAt(SB.length()-1);
                return SB.toString();
            }
            else if(!adj_list.containsKey(current_node)){
                continue;
            }
            else{
                for(String next_node : adj_list.get(current_node).keySet()){
                    if(visited.containsKey(next_node)){
                        continue;
                    }

                    LinkedHashMap<String, Boolean> next_visited = new LinkedHashMap<>();
                    for(String visited_node : visited.keySet()){
                        next_visited.put(visited_node, true);
                    }
                    //System.out.println(next_visited);
                    next_visited.put(next_node, true);
                    LinkedHashMap<String, LinkedHashMap<String,Boolean>> next_package = new LinkedHashMap<>();
                    next_package.put(next_node, next_visited);
                    to_visit.add(next_package);
                }
            }
        }

        return "no route found";
    }
    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);
        int n = Integer.parseInt(sc.nextLine());
        LinkedHashMap<String, LinkedHashMap<String, Boolean>> adj_list = new LinkedHashMap<>();

        for(int i = 0; i < n; i++){
            String[] splits = sc.nextLine().split(" ");
            String start_station = splits[0];
            
            // Bidirectional mapping:
            for(int j = 1; j < splits.length; j++){
                String next_station = splits[j];
                if(adj_list.containsKey(start_station)){
                    adj_list.get(start_station).put(next_station, true);
                }
                else{
                    LinkedHashMap<String, Boolean> innerHashMap = new LinkedHashMap<>();
                    innerHashMap.put(next_station, true);
                    adj_list.put(start_station, innerHashMap);
                }

                if(adj_list.containsKey(next_station)){
                    adj_list.get(next_station).put(start_station, true);
                }
                else{
                    LinkedHashMap<String, Boolean> innerHashMap = new LinkedHashMap<>();
                    innerHashMap.put(start_station, true);
                    adj_list.put(next_station, innerHashMap);
                }
            }
        }
        String[] splits = sc.nextLine().split(" ");
        String start_station = splits[0];
        String end_station = splits[1];
        System.out.println(BFS(start_station, end_station, adj_list));
    }
}
