import Boolean_Retrieval
import pprint
import json

# Crete New Instance
matrix = Boolean_Retrieval.Boolean_Retrieval()

# Input document collections
doc1 = matrix.add_documents('documents/doc1.txt')
doc2 = matrix.add_documents('documents/doc2.txt')
doc3 = matrix.add_documents('documents/doc3.txt')
doc4 = matrix.add_documents('documents/doc4.txt')

# merge word group list
matrix.get_word_group_list()

# generate dictionary
matrix.init_dictionary()

# search word each document in the dictionary 
matrix.search_word('documents/doc1.txt')
matrix.search_word('documents/doc2.txt')
matrix.search_word('documents/doc3.txt')
matrix.search_word('documents/doc4.txt')

# get inverted index
matrix.set_inverted_index()

# print results
incidence_matrix = json.dumps(matrix._incidence_matrix, sort_keys=True, indent=2)
inverted_index = json.dumps(matrix._inverted_index, sort_keys=True, indent=2)


print(matrix._incidence_matrix)
print(matrix._inverted_index)

print(incidence_matrix)
print("="*100)
print(inverted_index)

# save Files
with open("incidence_matrix.json", "w") as f:
  try:
    f.write(incidence_matrix)
    print("Updated incidence_matrix successfully")

  except:
    print("ERROR: json file can't be updated.")


with open("inverted_index.json", "w") as f:
  try:
    f.write(inverted_index)
    print("Updated inverted_index successfully")

  except:
    print("ERROR: json file can't be updated.")

