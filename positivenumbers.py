# -*- coding: utf-8 -*-
"""PositiveNumbers.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Gq-ed0azgI3_1_fvJUMtNF2bjwSRWOkX

Write a Python program to print all positive numbers in a range.
"""

n=int(input("Enter number of numbers in the list: ")) 
a = list(map(int,input("\nEnter the numbers : ").strip().split()))[:n]
for item in a:
  if item>0:
     print(item," ",end="")