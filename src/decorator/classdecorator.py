"""
There are two types of class decorator.
The first is:
    def decorator(C):
        # process class C
        return C
    
    @decorator    
    Class C:...         # C = decorator(C)
    
The second is:
    def decorator(C):
        # save or use class C
        return a differnt callable: nested func, class with __call__, etc.
        
    @decorator
    Class C:...         # C = decorator(C)



"""

def dcrGetAttr(cls):
    class Wrapper(object):
        def __init__(self,*args):
            self._cls = cls(*args)
            
        # Get known attribute will call this method
        def __getattr__(self,name):
            print('get attr:{0}'.format(name))
            return getattr(self._cls,name)
        
        # Get all attributes will call this method
        def __getattribute__(self,name):
            print('get attribute:{0}'.format(name))
            # if use below:
            # return getattr(self._cls,name)
            # then will get loop
            return object.__getattribute__(self,name)
    return Wrapper

@dcrGetAttr
class C(object):
    def __init__(self,x):
        self.attr = x

x = C('foo')    # x = dcrGetAttr(C)('foo')
print(x.attr)
x.unknownAttr = 'unknown'
print(x.unknownAttr)
