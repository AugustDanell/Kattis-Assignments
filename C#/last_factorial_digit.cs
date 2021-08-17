using System.IO;
using System;

class Program
{   
    static long accumulating_factorial(long n, long acc){
        if(n == 1 || n == 0){
            return acc;
        }
        else{
            return accumulating_factorial(n-1, n*acc);
        }
    }
    
    static void Main()
    {
        string line;
        line = Console.ReadLine();
        long iterations = Int64.Parse(line);
        
        // Using accumulating factorial (faster than normal) to get the last digit:
        while(iterations > 0){
            line = Console.ReadLine();
            long a = Int64.Parse(line);
            Console.WriteLine(accumulating_factorial(a, 1) % 10);    
            iterations --;
        }
    }
}
