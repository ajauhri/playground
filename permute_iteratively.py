#! /usr/bin/env python
import sys
# stl::next_permutation algorithm

def permute_iteratively(word):
    if len(word) == 0:
        print word
    else:
        first = reduce(lambda x,y : x+y, sorted(word))
        print first
        word = first
        end = len(word) - 1 
        i = end - 1
        while i >= 0:
            if word[i] < word[i+1]:
                j = end
                while not (word[i] < word[j]):
                    j -= 1
                new_word = word[:i] + word[j] + (word[i+1:j] + word[i] + word[j+1:])[::-1]
                print new_word
                word = new_word
                i = end - 1
            else:
                i -= 1

if __name__ == "__main__":
    permute_iteratively(sys.argv[1])
