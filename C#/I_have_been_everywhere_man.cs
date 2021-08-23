using System.IO;
using System;
using System.Collections.Generic;

class Program
{
    static void Main()
    {   
        string input;
        input = Console.ReadLine();
        long test_cases = Int64.Parse(input);
        
        // Iterating through each case:
        for(int i = 0; i < test_cases; i++){
            IDictionary<string, string> city_set = new Dictionary<string, string>();
            input = Console.ReadLine();
            long cities = Int64.Parse(input);
            
            // Iterating through each city:
            for(int j = 0; j < cities; j++){
                string city = Console.ReadLine();
                if(!city_set.ContainsKey(city)){
                    city_set.Add(city, "Exists");
                }
            }
            
            Console.WriteLine(city_set.Count);
        }
        
    }
}
