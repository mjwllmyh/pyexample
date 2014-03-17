
from collections import namedtuple
Point = namedtuple('Point',['x','y'],verbose=True)

p=[1,2]
d = Point._make(p)
print(d)

print(d._asdict())

print(d._replace(x=3))

