"""
"""

def wrapFunc(func):
    def wrapArgs(*args,**kwargs):
        return func(*args,**kwargs)
    return wrapArgs

@wrapFunc
def test1():
    print('test1')
    
@wrapFunc
def test2(input):
    print(input)
    
    
def wrapFuncWithArg(opt):
    print(opt)
    def wrapFunc(func):
        def wrapArgs(*args,**kwargs):
            return func(*args,**kwargs)
        return wrapArgs
    return wrapFunc

def wrapprint(opt):
    print(opt*2)
    def wrapFunc(func):
        def wrapArgs(*args,**kwargs):
            return func(*args,**kwargs)
        return wrapArgs
    return wrapFunc
 
@wrapFuncWithArg('opt')
def test3(input):
    print(input)

@wrapprint('opt1')
@wrapFuncWithArg('opt2')
def test3(input):
    print(input)
    
test1()    
test2('test2')
test3('true')
