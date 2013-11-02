"""
an example class used to show how to use 'property' decorator
"""

class C(object):
    def __init__(self):
        self._x = None
        
    @property
    def x(self):
        return self._x
    
    @x.setter
    def x(self,value):
        """
        if do not define this function, x will be read only
        """
        self._x = value
        
    @x.deleter
    def x(self):
        del self._x
        
if __name__ == '__main__':
    test = C()
    print(test.x)
    test.x = 10
    del test.x
    
    