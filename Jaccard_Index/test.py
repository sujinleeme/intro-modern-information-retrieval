import unittest
import jaccard_index as JI


class Test_Jaccard_Index(unittest.TestCase):
    def test_case_1(self):
        first_set = set(range(10))
        second_set = set(range(5, 20))
        res = JI.main(first_set, second_set)
        self.assertEqual(res, 0.25)

    def test_case_2(self):
        first_str = list("my home town is seoul, South Korea.")
        second_str = list("where is your home town?")
        k_gram = 2
        first_set = ngrams_split(first_str, k_gram)
        second_set = ngrams_split(second_str, k_gram)
        res = JI.main(first_set, second_set)
        self.assertEqual(res, 0.359)


def ngrams_split(lst, n):
    return set([''.join(lst[i:i + n]) for i in range(len(lst) - n)])


if __name__ == '__main__':
    unittest.main()
