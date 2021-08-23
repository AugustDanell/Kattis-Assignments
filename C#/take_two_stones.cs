using System.IO;
using System;

class Program
{
    static void Main()
    {
        string line;
        line = Console.ReadLine();
        long a = Int64.Parse(line);
        
        // Simple Modular arithmetic:
        if(a % 2 == 1){
            Console.WriteLine("Alice");
        }
        else{
            Console.WriteLine("Bob");
        }
    }
}
