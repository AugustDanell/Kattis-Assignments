using System.IO;
using System;

class Program
{
    static void Main()
    {
        string line;
        line = Console.ReadLine();
        long a = Int64.Parse(line);
        
        double sum = 0;
        while(a > 0){
            line = Console.ReadLine();
            int length = line.Length;
            long expo = Int64.Parse(new string(line[length-1], 1));
            string trimmed_line = line.Remove(length - 1, 1);
            long base_int = Int64.Parse(trimmed_line);
            
            sum += Math.Pow(base_int, expo); // The exponential expression
            a--;
        }
    Console.WriteLine(sum);
    }
}
