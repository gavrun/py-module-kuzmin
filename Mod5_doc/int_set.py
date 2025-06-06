"""
An implementation of the IntSet ADT
"""

class IntSet:
    '''
    Overview: An IntSet is a mutable, unbounded set of integers.
    E.g., {x1, x2, x3, ..., xn} with no duplicates.
    
    Abstract fields: x1, x2, x3, ..., xn
    
    >>> set1 = IntSet()
    >>> set1.add(9)
    >>> set1.size()
    1
    
    '''
    
    def __init__(self):
        '''
        Creator
        requires: none
        modifies: self 
        effects: creates and initizlizes a new empty IntSet
        throws: none
        returns: none
        '''
        self.check_rep()

        self.__data = []
        
        self.check_rep()
        
    
    def add(self, x):
        '''
        Mutator
        requires: x is an integer
        modifies: self 
        effects: self_post = self_pre U { x }
        throws: none
        returns: none
        '''
        self.check_rep()

        #if not x in self.__data and isinstance(x, int):
        self.__data.append(x)
        
        self.check_rep()
    
    def remove(self, x):
        '''
        Mutator
        requires: x is an integer
        modifies: self 
        effects: self_post = self_pre  \ { x }
        throws: none
        returns: none
        '''
        self.check_rep()

        self.__data.remove(x)
        
        self.check_rep()
    
    def print_set(self):
        '''
        Observer operation that prints elements of the IntSet
        
        requires: none
        modifies: none
        effects: none
        throws: none
        returns: none
        '''
        
        self.check_rep()

        print('{ ', end='')
        for elem in self.__data:
            print(elem, end=' ')
        print('}')
        
        self.check_rep()
    
    def contains(self, x):
        '''
        Observer
        requires: x is an integer
        modifies: none
        effects: none
        throws: none
        returns: none
        '''

        self.check_rep()
        
        return x in self.__data
    
    def size(self):
        '''
        Observer method that returns the size of the IntSet
        
        >>> set1 = IntSet()
        >>> set1.size()
        0

        >>> set1 = IntSet()
        >>> set1.add(9)
        >>> set1.size()
        1
        
        >>> set1 = IntSet()
        >>> set1.add(9)
        >>> set1.add(9)
        >>> set1.size()
        1
        
        requires: none
        modifies: none 
        effects: none
        throws: none
        returns: |self|
        '''

        self.check_rep()

        return len(self.__data)
    
    def get_elements(self):
        self.check_rep()
        
        return self.__data

    def check_rep(self):
        pass
        # for elem in self.__data:
        #     if not isinstance(elem, int):
        #         raise Exception('Non-integer in representation!')
        # set_data = set()
        # set_data.update(self.__data)
        # if len(set_data) != len(self.__data):
        #     raise Exception('Duplicates in representation!')

#if __name__ == '__main__':
# import doctest
# doctest.testmod()

#if __name__ == '__main__':
set1 = IntSet()
set1.add(1)
set1.add(1)
if set1.size() != 1:
    raise Exception('Potenital duplicates')
print('All custom unit tests passed.')
