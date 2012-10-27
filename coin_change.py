#! /usr/bin/env python
"""
Usage: coin_change [options]

Prints the minimum number of change using the input denominations.

Options:
-d, --provide a list of denominations. For example: coin_change 1 2 3
"""
from sys import argv, exit


def main():
    if not len(argv[1:]) > 1 and not argv[1] == "-d":
        print ("Please enter denominations.")
        exit()

    denominations_available = [ int(i) for i in argv[2:] ]
    value = input('Enter value (cents 0 - 99):')
    coin_change(value, denominations_available)

    
def coin_change(n, denominations):
    change_combinations = []
    change = dict((k,[]) for k in range(0,n+1))
    change[0] = [0]
    change_combinations.insert(0,0) 

    for i in range(1,n+1):
        change_combinations.insert(i,99999999999)
        for denomination in denominations:
            if i >= denomination and (1 + change_combinations[i - denomination]) < change_combinations[i]:
                change_combinations[i] = 1 + change_combinations[i - denomination]
        

    print change_combinations[n]        
 
     
if __name__ == "__main__":
    main()
