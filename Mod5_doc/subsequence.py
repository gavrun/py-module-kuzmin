
def subsequence(src, part):
    """
    @precondition
    src: is not None
    part: is not None
    @postcondition
    return value is false if part is not in src or if both src and part are []
                 is true if part is a partial match in the beginning or if len(part) == 0

    @parameters
    ----------
    src : must be iterable
        List in which we search.
    part : must be iterable
        Sublist that we are trying to find.

    @returns
    -------
    bool
        DESCRIPTION.

    """
    if (len(part) == 0):
        return True
    part_index = 0
    for elem in src:
        if elem == part[part_index]:
            part_index += 1
            if part_index == len(part):
                return True
        else:
            part_index = 0
    return False

# print(subsequence(None, None))
print(subsequence([],[]))
print(subsequence([1, 2],[]))
print(subsequence([],[3]))
print(subsequence((1, 2, 3, 2, 1, 5), (3, 2, 1)))
print(subsequence([1, 2, 3, 2, 1, 5], [3, 2, 1]))
print(subsequence(['a', 'b', 'c', 'f'], ['c', 'f']))
print(subsequence([1, 2, 3, 2, 1, 5], [1, 2, 3, 2, 1, 5, 6, 7]))
print(subsequence([1, 2, 3, 2, 1, 5], [2, 3, 3]))
print(subsequence([1, 2, 1, 2, 1, 3], [1, 2, 1, 3]))
