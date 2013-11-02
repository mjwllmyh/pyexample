# grep.py
#
# use yield as an expression
#
# Coroutine Execution
# When you call a coroutine, nothing happens
# They only run in response to next() and send() methods
#
# All coroutines must be "primed" by first calling .next() (or send(None))
# This advances execution to the location of the first yield expression

def grep(pattern):
    print "Looking for %s" % pattern
    while True:
        # Sent values are returned by (yield)
        line = (yield)
        if pattern in line:
            print line,

# Example use
if __name__ == '__main__':
    g = grep("python")
    g.next()
    g.send("Yeah, but no, but yeah, but no")
    g.send("A series of tubes")
    g.send("python generators rock!")
