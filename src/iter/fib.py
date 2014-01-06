import itertools

def fib():
    x,y = 0,1
    while True:
        yield x
        x,y = y,x+y
            
if __name__ == '__main__':
    for x in itertools.islice(fib(),10):
        print x