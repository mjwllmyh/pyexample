"""
Sort list by item's attribute.

The operator module also defines tools for generalized attribute
and item lookups. These are useful for making fast field extractors
as arguments for map(), sorted(), itertools.groupby(), or other
functions that expect a function argument.

operator.attrgetter(attr[, args...])

    Return a callable object that fetches attr from its operand.
    If more than one attribute is requested, returns a tuple of
    attributes. After, f = attrgetter('name'), the call f(b)
    returns b.name. After, f = attrgetter('name', 'date'), the
    call f(b) returns (b.name, b.date).

    The attribute names can also contain dots;
    after f = attrgetter('date.month'), the call f(b) returns b.date.month.


"""

import operator

def sortByAttr(inputList,attr):
    return sorted(inputList, key=operator.attrgetter)

print sortByAttr([{'id':0},{'id':1}],'id')
     