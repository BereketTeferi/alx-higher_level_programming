#!/usr/bin/python3
import sys

if __name__ == "__main__":  # Ensures code only runs when executed directly, not imported
   num_args = len(sys.argv) - 1  # Exclude the script name

   if num_args == 0:
       print("0 arguments.")
   else:
       print(f"{num_args} {'argument' if num_args == 1 else 'arguments'}:")
       for i in range(1, num_args + 1):
           print(f"{i}: {sys.argv[i]}")

