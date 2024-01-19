#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
   element1 = tuple_a[0] if len(tuple_a) >= 1 else 0
   element2 = tuple_a[1] if len(tuple_a) >= 2 else 0
   element3 = tuple_b[0] if len(tuple_b) >= 1 else 0
   element4 = tuple_b[1] if len(tuple_b) >= 2 else 0

   # Perform addition and return the resulting tuple
   return (element1 + element3, element2 + element4)
