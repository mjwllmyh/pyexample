"""class bake property()"""
#x = A()
#x.attr -> Property().__get__(x.attr, x, A)
#A.attr -> Property().__get__(A.attr, None, A)
    
class Property(object):
    def __init__(self, fget=None, fset=None, fdel=None, fdoc=None):
        self._fget = fget
        self._fset = fset
        self._fdel = fdel
        self._fdoc = fdoc
        
    def __get__(self, instance, owner):
        if self._fget is None:
            raise AttributeError, 'can not get attr'
        if instance is None:
            return self
        else:
            return self._fget(instance)
        
    def __set__(self, instance, value):
        if self._fset is None:
            raise AttributeError, 'can not set attr'
        # instance won't be None
        self._fset(instance, value)
            
    def __delete__(self, instance):
        if self._fdel is None:
            raise AttributeError, 'can not set attr'
        # instance won't be None
        return self._fdel()
    
class A(object):
    def __init__(self, attr):
        self._attr = attr
    def getAttr(self):
        return self._attr
    def setAttr(self, value):
        self._attr = value
    attr = Property(getAttr, setAttr)
        
x = A('apple')
A.attr = 'red apple'
print(A.attr)
