using System.IO;
using System;

class Program
{
    static void Main()
    {
        string line;
        line = Console.ReadLine();
        long a = Int64.Parse(line);
        double b = Math.Pow(2,a);
        b ++; 
        Console.WriteLine(b*b);
        
        
    }
}
