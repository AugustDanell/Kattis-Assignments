using System.IO;
using System;
using System.Collections.Generic;

class Program
{
    static void Main()
    {   
        int distinct = 0;    
        IDictionary<long, string> number_set = new Dictionary<long, string>();
        
        for(int i = 0; i < 10; i++){
            string input = Console.ReadLine();
            long num = Int64.Parse(input);
            num %= 42;
            
            if(!number_set.ContainsKey(num)){
                distinct ++;
                number_set.Add(num, "Exists");
            }
        }
        
        Console.WriteLine(distinct);
    }
}
