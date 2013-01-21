#!/usr/bin/env python
from collections import namedtuple
import sys
building = namedtuple('building', 'height pos')

def cal_flood(buildings):
    area = bldg_area = bt_area = 0
    stack = []
    last = lambda: stack[-1]
    first = lambda: stack[0]
    stack.append(building(buildings[0],1))

    for i,h in enumerate(buildings[1:]):
        i += 2
        if h > last().height:
            while last().height < h and len(stack) > 1:
                bldg_area += stack.pop().height
            # keep the largest if only one building exists in the stack
            if len(stack) == 1:
                if last().height > h:
                    pass 
                else:
                    bt_area = compute_area(last(), building(h,i))
                    if bldg_area < bt_area:
                        area += bt_area - bldg_area
                    bldg_area = 0
                    stack.pop()
        
        stack.append(building(h,i))
        print(stack)
    
    if len(stack) > 2:

        
    bt_area = compute_area(first(), last())
    if bldg_area < bt_area:
        area += bt_area - bldg_area
    return area


def compute_area(bldg_1, bldg_2):
    width = (bldg_2.pos - bldg_1.pos - 1)
    area = bldg_1.height * width if bldg_1.height < bldg_2.height else bldg_2.height * width
    return area

if __name__ == "__main__":
    a = sys.argv[1].split()
    arr = list(map(lambda x: int(x), a))
    print(cal_flood(arr))
