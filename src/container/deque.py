from collections import deque

d = deque('ghi')
d.appendleft('f')
d.popleft()
d.extendleft('abc')

def tail(filename, n=10):
    """Return the last n lines of a file"""
    return deque(open(filename), n)