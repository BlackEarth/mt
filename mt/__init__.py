
class MT(list):
    def __init__(self, s, *features):
        list.__init__(self, [Char(c) for c in s])
        self.features = features
    def __str__(self):
        return ''.join([str(char) for char in self])
    def __repr__(self):
        return "MT('%s')" % self

class Char:
    def __init__(self, c):
        assert len(c)==1 and type(c)==str
        self.c = c
    def __repr__(self):
        return "Char(%r)" % self.c
    def __str__(self):
        return self.c

class Range:
    def __init__(self, mt, char1, char2):
        self.mt = mt
        self.first = char1
        self.last = char2
    def __repr__(self):
        return "Range(%r, %r, %r)" % (self.mt, self.first, self.last)
    def __str__(self):
        return ''.join(str(self.mt)[self.mt.index(self.first):self.mt.index(self.last)+1])

class RangeList(list):
    pass

class Feature(dict):
    def __init__(self, *ranges, **args):
        dict.__init__(self, **args)
        self.ranges = RangeList(ranges)
    def __repr__(self):
        return "Feature(*%r, **%r)" % (self.ranges, {k:self[k] for k in self.keys()})

def tests():
    """
    >>> s1 = "This is the day that the Lord has made."
    >>> i1 = s1.index('d')
    >>> t1 = MT(s1); assert type(t1)==MT
    >>> assert str(t1)==str(s1)
    >>> n1 = t1[12]; n1
    Char('d')
    >>> assert str(n1)=='d'; assert (n1==Char('d'))==False
    >>> s2 = "good "
    >>> t2 = MT(s2); assert len(t2)==len(s2)
    >>> assert len([t1.insert(i1 + t2.index(n), n) for n in t2])==len(t2)
    >>> assert str(t1) == s1[:12] + s2 + s1[12:]
    >>> assert t1.index(n1) == i1 + len(t2)
    """

if __name__=='__main__':
    import sys
    if len(sys.argv) > 1:
        if sys.argv[1]=='test':
            import doctest
            doctest.testmod()