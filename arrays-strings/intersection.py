def intersection(a,b):
    item_set = set(a)
    return [items for items in b if items in item_set]

print(intersection([2,4,6,7,9], [6,7,9,24,33]))