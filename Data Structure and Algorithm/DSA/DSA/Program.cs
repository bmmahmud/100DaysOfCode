﻿using System;

namespace DSA
{
    class Program
    {
        
        static void Main(string[] args)
        {
           int[] arrayInput={1,2,4,5};
           // Console.WriteLine("Input values:");
            //int arrayInput = Convert.ToInt16(Console.ReadLine());

           // int number = Convert.ToInt16(Console.ReadLine());
           // Console.WriteLine("Fina {0}",number);

            int total;
            total = (arrayInput.Length+ 1) * (arrayInput.Length + 2) / 2;
            
                


            for (int i = 0; i < arrayInput.Length; i++)
            {
                
                    total -= arrayInput[i];       
            }
            Console.WriteLine("{0} is Miss", total);

        }
    }
}
