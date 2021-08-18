using System.IO;
using System;

class Program
{
    static void Main()
    {   
        long a;
        long b;
        string line;
        
        line = Console.ReadLine();
        string[] subs = line.Split(' ');
        
        a = Int64.Parse(subs[0]);
        b = Int64.Parse(subs[1]);
        
        if(a < b){
            Console.WriteLine(line);
        }
        else{
            string reversed = subs[1] + " " + subs[0]; // Attempting string concat.
            Console.WriteLine(reversed);
        }
    }
}
