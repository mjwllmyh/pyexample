class Context(object):
    """
    context classes implement two methods: __enter__ and __exit__.
    the variable after "as" is returned by __enter__.
    """
    def __enter__(self):
        print('entering')
        return self
        
    def __exit__(self,exception_type, exception_value,exception_traceback):
        print('exiting')
        if exception_traceback is None:
            print('with no error')
        else:
            print('with an error:'.format(exception_value))
        print('')
            
            
with Context():
    print('I am context')


with Context():
    print('I am context')
    raise TypeError('exception exists')

        