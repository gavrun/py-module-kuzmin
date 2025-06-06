def find(a, aLength, value):
    '''
    find() finds whether "value" in list "a" (of length "aLength") and returns
      the index of first "value" in "a". If "value" is not found in "a" then
      returns -1
    @requires: a is an iterable, all elements have the same type
              aLength is an integer,
              value has the same type as elements of a
    @modifies: None
    @effects: None
    @throws: ValueError, if len(a) != aLength
    @returns: the index of "value" in "a", if it is found, -1 otherwise
    '''
    res = -1
    i = 0
    if a is None:
        a = []
    if len(a) != aLength:
        raise ValueError()
    for i in range(aLength):
        if a[i] == value:
            return i
    
    return res

