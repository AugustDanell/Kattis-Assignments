import java.lang.Math; 
import java.util.*;

public class sok
{
 
  public static void main(String[] args)
  {
    Scanner sc = new Scanner (System.in);
  	String amount = sc.nextLine();
    String conc = sc.nextLine();
    
    double a,b,c,x,y,z;
    String[] splittedAmount = amount.split(" ");
    String[] splittedCon = conc.split(" ");
    
    a = Double.parseDouble(splittedAmount[0]);
    b = Double.parseDouble(splittedAmount[1]);
    c = Double.parseDouble(splittedAmount[2]);
    
    x = Double.parseDouble(splittedCon[0]);
    y = Double.parseDouble(splittedCon[1]);
    z = Double.parseDouble(splittedCon[2]);
    
    if((a/x) <= (b/y) && (a/x) <= (c/z)){
      orange(a,b,c,x,y,z);
    }
    else if((b/y) <= (a/x) && (b/y) <= (c/z)){
      apple(a,b,c,x,y,z);
    }
    else{
      pineapple(a,b,c,x,y,z);
    }
  }
  
  public static void print(double a, double b, double c){
    System.out.println(a + " " + b + " " + c);
  }
  
  public static void orange(double a, double b, double c, double x, double y, double z){
    double subValue = a/x;
    b -= subValue * y;
    c -= subValue * z;
    print(0.0, b, c);
  }
  
  public static void apple(double a, double b, double c, double x, double y, double z){
    double subValue = b/y;
    a -= subValue * x;
    c -= subValue * z;
    print(a, 0.0, c);
  }
  
  public static void pineapple(double a, double b, double c, double x, double y, double z){
    double subValue = c/z;
    a -= subValue * x;
    b -= subValue * y;
    
    print(a,b, 0.0);
  }
}
