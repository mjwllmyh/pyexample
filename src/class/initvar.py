"""
method for define attributes like below:

def __init__(self,a,b,c):
    self.a = a
    self.b = b
    self.c = c
    
"""

def attrFromDict(d):
    self = d.pop('self')
    for k,v in d.iteritems():
        setattr(self,k,v)
        

class C(object):
    def __init__(self,attrA,attrB,attrC):
        attrFromDict(locals())
        
    def __str__(self):
        return ' '.join((self.attrA,self.attrB,self.attrC))
        

if __name__ == '__main__':
    print(C('a','b','c'))