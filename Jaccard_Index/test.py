import unittest
import jaccard_index as JI


class Test_Jaccard_Index(unittest.TestCase):
    def test_case_1(self):
        first_set = set(range(10))
        second_set = set(range(5, 20))
        res = JI.main(first_set, second_set)
        self.assertEqual(res, 0.25)

    def test_case_2(self):
        first_str = "ides of March".lower().split()
        second_str = "“Caesar died in March".lower().split()
        first_set = set(first_str)
        second_set = set(second_str)
        res = JI.main(first_set, second_set)
        self.assertEqual(res, 0.167)

    def test_case_3(self):
        first_str = "My home town is seoul, south Korea.".lower()
        second_str = "Where is your home town?".lower()
        k_gram = 2
        first_set = ngrams_split(list(first_str), k_gram)
        second_set = ngrams_split(list(second_str), k_gram)
        res = JI.main(first_set, second_set)
        self.assertEqual(res, 0.368)


def ngrams_split(lst, n):
    return set([''.join(lst[i:i + n]) for i in range(len(lst) - n)])


if __name__ == '__main__':
    unittest.main()
