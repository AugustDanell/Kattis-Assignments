using System.IO;
using System;
using System.Linq;
using System.Text;

class Program
{
    static void Main()
    {
        string input = Console.ReadLine();
        long iterations = Int64.Parse(input);
        var builder = new StringBuilder();
        
        for(int i = 0; i < iterations; i++){
            input = Console.ReadLine();
            string[] split = input.Split(' ');
            
            if(split[0].Equals("Simon") && split[1].Equals("says")){
                builder.Append(input.Replace("Simon says", "") + "\n");
            }
        }
        
    
        Console.WriteLine(builder.ToString());
    }    
}
