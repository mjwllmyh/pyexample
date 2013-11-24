def insenstiveSort(stringList):
    return sorted(stringList, key=str.lower)

print(insenstiveSort(['a', 'B', 'c']))
