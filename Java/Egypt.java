import java.util.*;
import java.math.*;
//For my last submission i forgot to include the actual method that checked the input.
public class Egypt
{
  public static void pythchecker(int a, int b, int c){
    if((a*a) == (b*b)+(c*c)){
    	System.out.println("right");
    }
    else if((b*b) == (a*a)+(c*c)){
    	System.out.println("right");
    }
    else if((c*c) == (b*b)+(a*a)){
    	System.out.println("right");
    }
    else{
    	System.out.println("wrong");
    }
  }
  
  public static void main(String[]args){
    Scanner sc = new Scanner (System.in);
    boolean done = false;
    
    while(!done){
      String input = sc.nextLine();
      
      if(input.equals("0 0 0")){
        done = true; //Kan använda break istället men mer elegant så här.
      }
      else{
        String[] splitted = input.split(" ");
        int a = Integer.parseInt(splitted[0]);
        int b = Integer.parseInt(splitted[1]);
        int c = Integer.parseInt(splitted[2]);
        pythchecker(a, b, c);
        
      }
      
    }
  }
  
}