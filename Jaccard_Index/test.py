def jaccard_index(first_set, second_set):
    # If both sets are empty, jaccard index is defined to be 1

    index = 1.0
    if first_set or second_set:
        index = float(len(first_set.intersection(second_set)))/len(first_set.union(second_set))
        return index


first_set = set(range(10))
second_set = set(range(5, 20))
index = jaccard_index(first_set, second_set)
print(index) # 0.25 as 5/20




