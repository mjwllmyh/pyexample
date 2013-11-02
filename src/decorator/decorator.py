class myDecorator(object):
    """
    The only constraint upon the object returned by the decorator is that it
    can be used as a function which basically means it must be callable.
    Thus, any classes we use as decorators must implement __call__.
    """
    
    def __init__(self,func):
        print('inside myDecorator.__init__()')
        func()
        
    def __call__(self):
        print('inside myDecorator.__call__()')
        
@myDecorator
def _decoratorExecOrder():
    print('inside _decoratorExecOrder()')
    
_decoratorExecOrder()
#inside myDecorator.__init__()
#inside _decoratorExecOrder()
#inside myDecorator.__call__()
