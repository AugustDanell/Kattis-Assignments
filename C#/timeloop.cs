using System.IO;
using System;

class Program
{
    static void Main()
    {
        string line;
        line = Console.ReadLine();
        long a = Int64.Parse(line);
        long b = 1;
        
        while(a >= b){
            string output = String.Format("{0} Abracadabra", b);
            Console.WriteLine(output);
            b++;
        }
    }
}