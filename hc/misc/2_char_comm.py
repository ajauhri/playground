#! /usr/bin/env python
import sys
def comm_seq(str):
    """Returns the longest substring with 2 distinct characters
    
    :param string: input string
    :return   
    """
    str_len = len(str)
    dis_char_1 = ""
    dis_char_2 = ""
    max_length = curr_length = 0
    lst_char_seq = ""
    lst_char_seq_start = 0

    if str_len == 0 or str_len == 1:
        return []#raises InvalidStateException("String size is less or equal to 1") 
    else:
        curr_length += 1
        dis_char_1 = lst_char_seq = str[0]
        for i in range(1, str_len):
            if str[i] == dis_char_1:
                curr_length += 1

            elif dis_char_2 == "":
                dis_char_2 = str[i]
                curr_length += 1
            
            elif str[i] == dis_char_2:
                curr_length += 1

            else:
                max_length = max(max_length, curr_length)
                curr_length = i - lst_char_seq_start + 1
                dis_char_1 = lst_char_seq
                dis_char_2 = str[i]
           
            if str[i] != lst_char_seq:
                lst_char_seq_start = i
                lst_char_seq = str[i]

        max_length = max(max_length, curr_length)
        return max_length

if __name__ == "__main__":
    print(comm_seq(sys.argv[1]))
