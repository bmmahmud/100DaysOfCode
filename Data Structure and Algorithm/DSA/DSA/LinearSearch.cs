﻿using System;
using System.Collections.Generic;
using System.Text;

namespace DSA
{
    class LinearSearch
    {
        static void Main(string[] args)
        {
            int[] arr = {3, 5, 6, 4};
            Console.WriteLine("Input values:");
            int arrayInput = Convert.ToInt16(Console.ReadLine());

            int number = Convert.ToInt16(Console.ReadLine());
            Console.WriteLine("Fina {0}", number);
            for (int i = 0; i < arrayInput; i++)
            {
                if (arr[i] == number)
                {
                    Console.WriteLine("{0} is Present at Index {1}", number, i + 1);
                    break;
                }

                if (i == number)
                {
                    Console.WriteLine("{0} is Not Present in Array", number);
                }
            }
        }
    }
}
