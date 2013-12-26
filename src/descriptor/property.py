"""
class bake property()
"""

class Property(object):
    """
    """
    def __init__(self,fget=None,fset=None,fdel=None,fdoc=None):
        self._fget=fget
        self._fset=fset
        self._fdel=fdel
        self._fdoc=fdoc
        
    def __get__(self,instance,owner=None):
        if self._fget is None:
            raise AttributeError,'can not get attr'
        if instance is None:
            pass
        
    def __set__(self,instance,value):
        if self._fset is None:
            raise AttributeError,'can not set attr'
        if instance is None:
            self
            
    def __delete__(self,instance):
        if self._fdel is None:
            raise AttributeError,'can not set attr'
        return self._fdel
    
class A(object):
    def __init__(self,attr):
        self._attr = attr
        
    def getAttr(self):
        return self._attr
    
    def setAttr(self,value):
        self._attr = value
        
    attr = Property