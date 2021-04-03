#!/usr/bin/python
def isListOfInts(x) -> bool:
    if(type(x) != list):
        raise ValueError(str(x) + " - arg not of <list> type")

    return all(type(i) == int for i in x)


def testList(a):
    print(isListOfInts(a))


testList([])
testList([1])
testList([1, 2])
testList([0])
testList(['1'])
testList([1, 'a'])
testList(['a', 1])
testList([1, 1.])
testList([1., 1.])
testList((1, 2))
