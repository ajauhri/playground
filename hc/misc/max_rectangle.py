#! /usr/bin/env python
from collections import namedtuple

Block = namedtuple('Block', 'start height')
def max_rectangle(h):
    max_area = 0
    stack = []
    top = lambda: stack[-1]
    pos = 0
    for pos, height in enumerate(h):
        start = pos
        while True:
            print(stack,max_area)
            if not stack or height > top().height:
                stack.append(Block(start, height))
            elif height < top().height:
                max_area = max(max_area, top().height * (pos - top().start))
                start, _ = stack.pop()
                continue
            break
    pos += 1
    for start, height in stack:
        max_area = max(max_area, height*(pos - start))
    return max_area

if __name__ == "__main__":
    print(max_rectangle([2,4,2,1]))
