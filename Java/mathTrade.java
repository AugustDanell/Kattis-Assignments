import java.util.Scanner;
import java.util.HashMap;

/*   mathTrade 738th Kattis
*    Assignment here: https://open.kattis.com/problems/mathtrade
*    Just iterate over every person and create the largest chain by accessing over HashMap. 
*/

public class mathTrade {
    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);
        int ppl = Integer.parseInt(sc.nextLine());
        HashMap<String, String> item_mapping = new HashMap<>();
        for(int i = 0; i < ppl; i++){
            String[] items = sc.nextLine().split(" ");
            item_mapping.put(items[1], items[2]);
        }

        int max_count = 0;
        for(String start_item: item_mapping.keySet()){
            int count = 0;
            String want = start_item;
            HashMap<String, Boolean> visited = new HashMap<>();
            //System.out.println("Start:" + start_item);
            
            while(item_mapping.containsKey(want)){
                want = item_mapping.get(want);
                count ++;
              //  System.out.println("Want: " + want);
                if(want.equals(start_item)){
                    break;
                }
                else if(visited.containsKey(want)){
                    count = 0;
                    break;
                }
                
                visited.put(want, true);
            }
            
            //System.out.println("Hold: " + want);
            if(!item_mapping.containsKey(want) || !(start_item.equals(want))){
                //System.out.println("Test: " + start_item + " " + item_mapping.get(want));
                count = 0;
            }
            max_count = Math.max(max_count, count);
            //System.out.println();

        }

        if(max_count == 0){
            System.out.println("No trades possible");
        }
        else{
            System.out.println(max_count);
        }
    }
    
}
