"""
>>> class Descriptor(object):
...     def __get__(self, instance, owner):
...         print(self, instance, owner, sep='\n')
...
...
>>> class Subject:
...    attr = Descriptor()   # Descriptor instance is class attr         
...
...
>>> X = Subject()
>>> X.attr
<__main__.Descriptor object at 0x0281E690>
<__main__.Subject object at 0x028289B0>
<class '__main__.Subject'>
>>> Subject.attr
<__main__.Descriptor object at 0x0281E690>
None
<class '__main__.Subject'>


How to make attribute read only:
>>> class D:
...    def __get__(*args): print('get')
...    def __set__(*args): raise AttributeError('cannot set')
...
...
>>> class C:
...    a = D()
...
...
>>> X = C()    # Routed to C.a.__get__
>>> X.a    # Routed to C.a.__set__
get
>>> X.a = 99
AttributeError: cannot set

"""

class Subject(object):
    """
    """
    class Descriptor(object):
        """
        descriptor docs
        """
        def __get__(self,instance,owner):
            """
            :Parameters:
                self: `instance`
                    class's instance
                instance: `instance`
                    The instance that attribute belongs.
                    For class.attr, it is None.
                    For instance.attr, it is instance.
                owner: `class`
                    the class that descriptor's instance will add to
            """
            print('Get...')
            return instance._attr
            
        def __set__(self,instance,value):
            print('Set...')
            instance._attr = value
             
        def __delete__(self,instance):
            print('Delete...')
            del(instance._attr)
    
    def __init__(self,attr=''):
        self._attr = attr
        
    # X.attr -> Descriptor.__get__(Subject.attr, X, Descriptor)
    attr = Descriptor()
    
if __name__ == '__main__':
    objA = Subject('1')
    objA.attr = 'Apple'
    print('objA attr:{0}'.format(objA.attr))
    # objA.attr -> Descriptor.__get__(Subject.attr, objA, Descriptor)
    # Set...
    # Get...
    # objA attr:Apple
    
    print('Class attr:{0}'.format(Subject.attr))
    # Subject.attr -> Descriptor.__get__(Subject.attr, None, Descriptor)
    # Get...
    # AttributeError: 'NoneType' object has no attribute '_attr'
    
    
