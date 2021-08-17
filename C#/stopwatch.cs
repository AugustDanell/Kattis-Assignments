using System.IO;
using System;

class Program
{   
    static void Main()
    {
        string line;
        line = Console.ReadLine();
        long stops = Int64.Parse(line);
        
        if(stops % 2 == 1){
            Console.WriteLine("Still running");
        }
        else{
            bool start = true;
            long previousValue = 0;
            long totalTime = 0;
            
            while(stops > 0){
                line = Console.ReadLine();
                long currentValue = Int64.Parse(line);
                   
                if(start){
                    previousValue = currentValue;
                    start = false;
                }
                else{
                    totalTime += currentValue - previousValue;                    
                    start = true;
                }
                
                stops --;
            }
        
            Console.WriteLine(totalTime);
        }
    }
}
