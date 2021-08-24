using System.IO;
using System;
using System.Collections;

class Program
{
    static void Main()
    {   
        string data_sequence = Console.ReadLine();
        char[] char_arr = data_sequence.ToCharArray();
        ArrayList index_list = new ArrayList();
        
        for(int i = 0; i < char_arr.Length; i++){
            if(char_arr[i] == ':' || char_arr[i] == ';'){
                // Make a check
                if(i < char_arr.Length-2){
                    if(char_arr[i+1] == '-' && char_arr[i+2] == ')'){
                        index_list.Add(i);
                    }
                }
                
                if(i < char_arr.Length-1 && char_arr[i+1] == ')'){
                    index_list.Add(i);
                }
                
            }    
        }
        
        foreach(var index in index_list){
            Console.WriteLine(index);
        }
    }
}
