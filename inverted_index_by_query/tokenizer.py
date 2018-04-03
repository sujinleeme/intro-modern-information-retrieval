#!/usr/bin/env python
# encoding: utf-8

"""
A simple tokenizer.
"""

import codecs
import re
import sys


def tokenize(text):
    """
    Applies regular expressions to extract tokens from a string.
    """
    
    div_pattern = r"""
                  (?:\d+\.\d+\.\d+)|(?:\d+\.\d+)  # Date
                 |\d{1,2}:\d{2}                   # Time
                 |\d+(?:\.\d+)*(?:,\d+)?          # Number
                 |\w+(?:[-]\w+)*                  # Word (possibly compound)
                 |[\(\)"]                         # Parentheses
                 |[\.,?!]                         # Punctuation
                 |[^\s]+                          # Other
                  """

    
    token_pattern = re.compile(div_pattern, re.VERBOSE|re.UNICODE)
    
    return token_pattern.findall(text)


def get_number_of_different_tokens(token_list):
    """
    Calculates the number of different tokens in a text.
    """
    
    return len(set(token_list))
    
##  
##def main():
##    """
##    Reads a file, splits it into tokens and outputs them.
##    """
##    
##    # File name of the file to be processed.
##    if len(sys.argv) < 2:
##        print "Usage: python tokenizer.py FILENAME"
##        exit()
##    else:
##        input_file_name = sys.argv[1]
##    
##    text = codecs.open(input_file_name, encoding="utf-8").read()
##
##    tokens = tokenize(text)
##    for token in tokens:
##        print token.encode('utf8')
##
##    print "\nNumber of Tokens: %d" % get_number_of_different_tokens(tokens)
##
### Call the main function
##if __name__ == "__main__":
##    main()

