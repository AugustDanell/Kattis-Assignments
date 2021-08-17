using System.IO;
using System;

class Program
{
    static void Main()
    {
        string line;
        line = Console.ReadLine();
        long x = Int64.Parse(line);
    
        line = Console.ReadLine();
        long y = Int64.Parse(line);
        
        if(x > 0 && y > 0){
            Console.WriteLine("1");
        }
        else if(x > 0 && y < 0){
            Console.WriteLine("4");
        }
        else if(x < 0 && y > 0){
            Console.WriteLine("2");
        }
        else{
            Console.WriteLine("3");
        }
    }
}
