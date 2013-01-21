#!/usr/bin/env python
import sys
def reverse(string):
    print(string)
    l = len(string) - 1 
    for i in range(int(l/2+1)):
        c = string[i]
        string[i] = string[l]
        string[l] = c
        l -= 1
    return string

if __name__ == "__main__":
    string = list(map(lambda x: x, sys.argv[1]))
    string = reverse(string)
    string.append(' ')
    word_len = 0
    for i in range(len(string)):
        if string[i] != ' ':
            word_len += 1
        else:
            string[i-word_len:i]=reverse(string[i-word_len:i])
            word_len = 0
    string = string[:-1]
    string = "".join(string)
    print(string)
    
