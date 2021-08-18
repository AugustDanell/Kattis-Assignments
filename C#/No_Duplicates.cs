using System.IO;
using System;
using System.Collections;

class Program
{
    static void Main()
    {   
       string line = Console.ReadLine();
       string[] subs = line.Split(' ');
       ArrayList myAL = new ArrayList();
       
       int i = subs.Length-1;
       bool found_duplicate = false;
       
       // Working the other way, back to front, but works just as well:
       while(i >= 0){
           string current = subs[i];
           if(myAL.Contains(current)){
               found_duplicate = true;
               Console.WriteLine("no");
               break;
           }
           
           myAL.Add(current);
           i--;
       }
        
       if(!found_duplicate){
           Console.WriteLine("yes");
       }
    }
}
