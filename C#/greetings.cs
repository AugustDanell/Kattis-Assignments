using System.IO;
using System;
using System.Linq;
using System.Text;

class Program
{
    static void Main()
    {   
        string hey;
        hey = Console.ReadLine();
        
        var builder = new StringBuilder();
        
        for(int i = 0; i < hey.Length-2; i++){
            builder.Append("ee");
        }
        
        string msg = builder.ToString();
        msg = msg.Insert(0, "h");
        msg = msg.Insert(msg.Length, "y");
        
        Console.WriteLine(msg);
        
    }
}
