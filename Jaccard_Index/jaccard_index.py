from typing import Set


def jaccard_index(first_set: Set, second_set: Set) -> Set:
    # If both sets are empty, jaccard index is defined to be 1
    index = 1.0
    if first_set or second_set:
        index = float(len(first_set.intersection(second_set))) / len(first_set.union(second_set))
        return index


def main(first_set, second_set):
    res = jaccard_index(first_set, second_set)
    print("first set: {first_set}\n"
          "second set: {second_set}\n"
          "jaccard_index: {res}"
          .format(first_set=first_set, second_set=second_set, res=res))
    return res


if __name__ == '__main__':
    main()
