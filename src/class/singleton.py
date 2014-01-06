"""
There are four types.
1. Use '__new__' method
2. Share attribute (Brog)
"""
class Singleton(object):
    def __new__(cls,*args,**kwargs):
        if not hasattr(cls,'_inst'):
            cls._inst = super(Singleton,cls).__new__(cls,*args,**kwargs)
        else:
            print('has been created.')
        return cls._inst

    
class C(Singleton):
    classAttr = ''
    def __init__(self,attr):
        self.attr = attr
        
    def __str__(self):
        return self.attr


class Borg(object):
    _shared_state = {}
    def __new__(cls,*args,**kwargs):
        obj = object.__new__(cls,*args,**kwargs)
        obj.__dict__ = cls._shared_state
        return obj
    
    
def singleton(cls):
    _inst = {}
    def _wrap(*args,**kwargs):
        if cls not in _inst:
            _inst[cls] = cls(*args,**kwargs)
        return _inst[cls]
    return _wrap
        
        
@singleton
class D(Singleton):
    classAttr = ''
    def __init__(self,attr):
        self.attr = attr
        
    def __str__(self):
        return self.attr
    
    
if __name__ == '__main__':
    objA = C('Tom')
    print(id(objA))
    print(objA.attr)
    objA.name = 'A'
    objA.classAttr = 'A'
    
    objB = C('Jerry')
    print(id(objB))
    objB.name = 'B'
    objB.classAttr = 'B'
    print(objB.attr)
    print(objA.name)
    print(objA.classAttr)
    
    objA = D('Tom')
    print(id(objA))
    print(objA)
    objA.name = 'A'
    objA.classAttr = 'A'
    
    objB = D('Jerry')
    print(id(objB))
    objB.name = 'B'
    objB.classAttr = 'B'
    print(objB.attr)
    print(objA.name)
    print(objA.classAttr)    
    
        

            