from collections import OrderedDict

def sortByKeys(dictionary):

  if type(dictionary) != dict:
    raise TypeError("input must be dictionary.")
  
  return OrderedDict((k, v) for k, v in sorted(dictionary.items(), key=lambda x: x[0]))