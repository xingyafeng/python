import logging
from collections import deque

def test_list_features():
    # type: () -> test_list_features()
    """
    :rtype: object
    """
    logging.debug("test list ...")

    a = [1, 2, 3, 4, 5, 5, 5, ]
    print a

    a.reverse()
    print a
    a.sort()
    print a

    a.append('dd')
    print a
    a.pop()
    print a

    quene = deque(["a", "b", "c"])
    quene.append("d")
    quene.append("e")
    print quene.popleft()
    print quene
    del quene[2]
    print quene

    for i, v in enumerate(['a', 'b', 'c']):
        print i, v
