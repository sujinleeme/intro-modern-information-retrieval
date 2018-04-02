#!/usr/bin/python
# -*- coding: utf-8 -*-

# A term-document incidence matrix.
import re
from collections import OrderedDict
from utils import sortByKeys

class Document():
  def __init__(self):
    self._wordlist = []
  
  def tokenize(self, filename):
    content = open(filename, "r").read().lower().split()
    self._wordlist.extend(content)

class Boolean_Retrieval():
  def __init__(self):
    self._docs = {}
    self._dictionary = {} # a dictionary of terms
    self._incidence_matrix = {} # term-document sincidence matrix for document collection.
    self._inverted_index = {} # inverted index representation for collection

  def add_documents(self, doc):
    if doc not in self._docs:
      self._docs[doc] =  Document()
      self._docs[doc].tokenize(doc)

  # building an index by sorting adnd grouping 
  def get_word_group_list(self):
    word = [value._wordlist for key, value in self._docs.items()] 
    word = set(sum(word, []))
    self._dictionary = sorted(word, reverse=False)

  # make dictionary format to set document Id to store word counting results
  def init_dictionary(self):
    init_doc_id = dict([(re.findall(r'[ \w-]+?(?=\.)', key)[0]
                      , 0) for key in self._docs.keys()])
    dictionary = dict([(key, init_doc_id) for key in self._dictionary])
    self._incidence_matrix = sortByKeys(dictionary)
  
  def search_word(self, filename):
    doc_id = re.findall(r'[ \w-]+?(?=\.)', filename)[0]
    wordlist = self._docs[filename]._wordlist
    for word in wordlist:
        if word in self._incidence_matrix.keys():
          context = {}
          context.update(self._incidence_matrix[word])
          context[doc_id] +=1
          self._incidence_matrix[word] = context

  def set_inverted_index(self):
    if self._incidence_matrix:
      index = {}
      for word in self._incidence_matrix:
        docs = self._incidence_matrix[word]
        filter_docs = {word: sorted([i for i,j in docs.items() if j > 0])}
        index.update(filter_docs)
      self._inverted_index = sortByKeys(index)