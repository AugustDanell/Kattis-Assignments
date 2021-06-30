import java.util.*;
// Solution to the problem "Death Knight Hero".
public class dk
{
  public static void main(String[] args)
  {
    Scanner sc = new Scanner (System.in);
    int cases = sc.nextInt();
    sc.nextLine();
    
    int sum = 0;
    for(int i = 0; i < cases; i++){
    	String input = sc.nextLine();
        sum += rightOrder(input);
    }
    
    System.out.println(sum);
  }

  public static int rightOrder(String input){
    for(int i = 0; i < input.length() - 1; i++){
      if(input.charAt(i) == 'C' && input.charAt(i+1) == 'D'){
        return 0;
      }
    }
    
    return 1;
  }
}
