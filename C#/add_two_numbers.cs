using System.IO;
using System;

class Program
{
    static void Main()
    {   
        string input;
        input = Console.ReadLine();
        string[] split = input.Split(' ');
        
        long a = Int64.Parse(split[0]);
        long b = Int64.Parse(split[1]);
        
        Console.WriteLine(a+b);
    }
}
