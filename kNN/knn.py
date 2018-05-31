#!/usr/bin/python
# -*- coding: utf-8 -*-
# 2019.05.31
# Sujin Lee

import math
import os
import sys
from re import *
from operator import itemgetter
import time

start = time.time()

def tokenize(input_text):
    '''Returns a list of words in the input text.'''

    # input_text = input_text.decode('latin1')

    # English clitics.
    input_text = input_text.replace("'ll", " will")
    input_text = input_text.replace("'re", " are")
    input_text = input_text.replace("'ve", " have")
    input_text = input_text.replace("won't", "will not")
    input_text = input_text.replace("n't", " not")
    input_text = input_text.replace("'m", " am")

    # Convert single text lines to fluent text and lower the letters.
    input_text = input_text.lower()

    # Regex to search for words.
    # IMPORTANT: The search regex and the string to search in have to be
    # unicode, otherwise it will not work properly.
    re_words = compile("[abcdefghijklmnopqrsšzžtuvwõäöüxy'-]+",
                       IGNORECASE | MULTILINE | DOTALL)

    # Now the words can be extracted.
    text_word_list = re_words.findall(input_text)

    return text_word_list


# Calculates the length of a vector.
def calculate_vector_length(vector):
    # Your code goes here
    vector_length = math.sqrt(sum([v ** 2 for v in vector]))+ sys.float_info.epsilon
    return vector_length


# Calculates the Euclidean distance between vector_1 und vector_2.
def calculate_euclidean_distance(vector_1, vector_2):
    # Your code goes here
    distance = math.sqrt(sum([(a - b) ** 2 for a, b in zip(vector_1, vector_2)])) + sys.float_info.epsilon

    return distance


def create_index(docs_dict):
    """Create postings list for faster access of Document Frequency."""
    """
        index 
            key: token
            value: array with file names

        Example
        {'shop': ['00042_ham.txt'], 'confirmation': ['00047_spam.txt'],
            'very': ['00037_spam.txt', '00049_spam.txt']}

    """

    term_index = {}
    # Your code goes here
    for txt in docs_dict:
        for token in docs_dict[txt][1]:
            if token in term_index:
                term_index[token].append(txt)

            if token not in term_index:
                term_index[token] = [txt]

    return term_index


def get_stop_word_list():
    """Returns the list of stop words."""

    in_f = open("stopwords.txt")
    stop_words = in_f.read().strip().split("\n")
    in_f.close()

    return stop_words


def create_document_vectors(training_folder):
    """
    Computes the document vectors for documents from the training data
    and return them and the general document vector.
    """

    """
    docs_dict
        Key: Training file name
        Value: Array of length 2 (Lets call this array 'A')

        Array 'A'
            Length: 3
            A[0]: 'ham' or 'spam'
            A[1]: Another array with tokens from the file (no stopwords in this array)
            A[2]: Array with tf-idf values

        Example of docs_dict
        {'00043_ham.txt': ['ham', ['thank', 'posting', 'same', 'issue', 'listmaster', 'lists', 'debian', 'org'], [0.0, 0.0, 0.0, 0.0, 0.0, 0.2011798118406769, 0.0, 0.2011798118406769, 0.0, 0.0, 0.0, 0.0, 0.2011798118406769]}

    document_vector
        Array of all distinct tokens in the training set (no stop words)

    """
    docs_dict = {}

    # Your code goes here
    # Read in and tokenize each document of the training data. Remember to remove stop words.

    for txt in os.listdir(training_folder):
        t = open("%s/%s" % (training_folder, txt), encoding='utf-8')
        doc_tokens = tokenize(t.read())

        # Remove stop words from doc_tokens
        doc_class, doc_tokens = remove_stop_words(doc_tokens)

        # Add to docs_dict
        docs_dict[txt] = [doc_class, doc_tokens]

        t.close()


    # Generate term_index while reading in each document from training_folder
    term_index = create_index(docs_dict)

    # Create tf-idf weighted document vector. You will need to use document frequency values from create_index.
    docs_terms = sorted(term_index.keys())

    total_docs_num = len(docs_dict.keys())

    for doc in docs_dict:
        doc_vect = []
        for term in docs_terms:
            tf = docs_dict[doc][1].count(term)
            df = len(term_index[term])
            tf_idf = tf * math.log10(total_docs_num) / df
            doc_vect.append(tf_idf)
        docs_dict[doc].append(doc_vect)

    # Normalize vector
    docs_vector = []
    for doc in docs_dict:
        vectors = docs_dict[doc][2]
        denominator = calculate_vector_length(vectors)
        norm = [v/denominator for v in vectors]
        docs_dict[doc][2] = norm
        docs_vector.append(norm)


    return docs_dict, docs_terms, term_index, docs_vector


def remove_stop_words(tokens):
    stop_words = get_stop_word_list()
    tokens = [x for x in tokens if x not in stop_words]
    return tokens[0], tokens[1:]


def remove_stop_words_test_document(tokens):
    stop_words = get_stop_word_list()
    tokens = [x for x in tokens if x not in stop_words]
    return tokens

def create_test_document_vector(docs_dict, test_document, document_terms, index):
    # Process test document.
    in_f = open(test_document)
    doc_tokens = tokenize(in_f.read())

    # Remove stop words from doc_tokens
    doc_class, doc_tokens = remove_stop_words(doc_tokens)

    # Add token array to doc_class array
    doc_data = [doc_class, doc_tokens]

    in_f.close()

    """
    doc_data should now look like this:
        Type: Array
        Size: 2
        doc_data[0]: 'spam' or 'ham'
        doc_data[1]: array of tokens (with stop words removed)

    doc_vect
        Type: Array with tf-idf values
        Example
        [0.11856790094712363, 0.0, 0.0, 0.0, 0.0, 0.39387404130807196, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.27530614036094825]
    """
    doc_vect = []

    # Create tf-idf weighted document vector using document_terms
    for term in document_terms:
        tf = doc_data[1].count(term)
        df = len(index[term])
        doc_vect.append(tf * math.log10(len(docs_dict.keys()) / df))

    # Normalize the vector.
    denominator = calculate_vector_length(doc_vect)
    norm = [v/denominator for v in doc_vect]

    doc_vect = norm
    return doc_data, doc_vect


# Main program.
if __name__ == "__main__":

    if len(sys.argv) < 4:
        print("Usage: python knn.py train test_file k")
    else:

        training_folder = sys.argv[1]
        test_document = sys.argv[2]
        k = int(sys.argv[3])

        docs_dict, docs_terms, term_index, docs_vector = create_document_vectors(training_folder)
        print("Total: ", len(docs_terms))
        test_doc_data, test_doc_vector = create_test_document_vector(docs_dict, test_document, docs_terms, term_index)

        # Calculate the Euclidean distance of the test document to training documents.
        distances = {}
        spam_cnt = 0
        ham_cnt = 0
        print("Calculating Euclidean distance between the new document and the training documents ...")

        for doc_vector, txt in zip(docs_vector, docs_dict):
            distances[txt] =  calculate_euclidean_distance(doc_vector, test_doc_vector)

        # Sort nearest docs and their distances to the new document.
        sorted_distances = sorted(distances.items(), key=itemgetter(1))

        # Calculate the majority class of the nearest neighbours
        final_label = ''
        docs_class = [docs_dict[doc[0]][0] for doc in sorted_distances[0:k]]
        spam_cnt = docs_class.count('spam')
        ham_cnt = docs_class.count('ham_cnt')

        if (spam_cnt >= ham_cnt):
            final_label = 'spam'
        else:
            final_label = 'ham'

        # Show the results.
        print("Assigned class: %s" % final_label)

        if test_doc_data[0] == final_label:
            print("Correct class assigned to new document! :-)")
        else:
            print("Wrong class assigned to new document! :-(")

        print("Nearest neighbours:")

        for doc in sorted_distances[0:k]:
            print(doc)

end = time.time()
print("Time duration: %2.2f" % (end-start))