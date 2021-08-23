using System.IO;
using System;

class Program
{
    static void Main()
    {
        string input = Console.ReadLine();
        string[] split = input.Split(' ');
        
        // Double works similar to ints, they can use the INT64 parse or their own (total problems willbe an integer anyways): 
        double total_problems = Int64.Parse(split[0]);
        double problems = Int64.Parse(split[1]);
        double problem_residual = 3*(total_problems - problems);
        double sum = 0;
        
        for(int i = 0; i < problems; i++){
            sum += Double.Parse(Console.ReadLine());
        }
        
        
        double min = (sum - problem_residual)/total_problems;
        double max = (sum + problem_residual)/total_problems;
        
        // To do a format string we write the number of the one we want in braces {}:
        Console.WriteLine("{0} {1}", min, max);
    }
}
