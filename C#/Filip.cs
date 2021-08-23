using System.IO;
using System;

class Program
{   
    
    public static string Rev( string s )
    {
        char[] charArray = s.ToCharArray();
        Array.Reverse( charArray );
        return new string( charArray );
    }
    
    static void Main()
    {   
        string input;
        input = Console.ReadLine();
        string[] split = input.Split(' ');
        
        long a = Int64.Parse(Rev(split[0]));
        long b = Int64.Parse(Rev(split[1]));
        
        if(a > b){
            Console.WriteLine(a);
        }
        else{
            Console.WriteLine(b);
        }
    }
}
