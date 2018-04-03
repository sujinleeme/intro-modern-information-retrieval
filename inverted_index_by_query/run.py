import re
import os
import tokenizer


# folder containing text documents should be named 'files'
# the 'files' folder should be in the same directory as this .py file.


def make_inverted_index(input_folder):
    '''
    Opens text files in a specified folder, normalizes them using the tokenizer
    and adds all the tokens found in the documents to the inverted index.
    '''

    files_data = {}
    inverted_index = {}

    # Go through the files subfolder and read in all text files in it.
    for fn in os.listdir(input_folder):
        # Read contents of text files.
        f = open("%s/%s" % (input_folder, fn), encoding='utf-8')
        files_data[fn] = f.read()
        f.close()

    # Dictionary to keep track which document corresponds to which id.
    doc_id_mapping = {}
    files_names = sorted([x for x in files_data.keys()], reverse=False)
    doc_id_mapping = dict(list(enumerate(files_names)))

    # The entire text for each document is now saved in 'files_data'.
    # Now tokenize each document using 'tokenizer.tokenize'
    # Don't forget to use .lower() function before tokenizing the text
    for file in files_data:
        tokenized_str = [x.lower() for x in tokenizer.tokenize(files_data[file])]
        files_data[file] = tokenized_str

    # Code to create inverted index goes here
    all_terms = [value for value in files_data.values()]
    sort_terms = sorted(set(sum(all_terms, [])), reverse=False)

    # Init Dictionary
    set_docs_title = dict([(x, 0) for x in doc_id_mapping.values()])
    incidence_matrix = dict([(key, set_docs_title) for key in sort_terms])

    # Count word each document and generate incidence matrix
    docs_titles = [x for x in doc_id_mapping.values()]
    for title in docs_titles:
        for term in incidence_matrix:
            if term in files_data[title]:
                context = {}
                context.update(incidence_matrix[term])
                context[title] += 1
                incidence_matrix[term] = context

    # Find document ID number
    def find_doc_number(dict, value):
        return [num for num, title in dict.items() if title == value][0]

    # Generate Inverted Index
    for term in incidence_matrix:
        docs = incidence_matrix[term]
        filter_docs = {term: sorted([find_doc_number(doc_id_mapping, i) for i, j in docs.items() if j > 0])}
        inverted_index.update(filter_docs)

    return inverted_index, doc_id_mapping


def process_simple_query(query, inverted_index, doc_id_mapping):
    '''Returns the postings list (and the corresponding document names)
    for a one-word query.'''

    # Code to process a one-word query goes here
    # Nothing needs to be returned. Simply print the results.
    result = inverted_index[query]

    for docID in result:
        print("Term '{term}' found in document {docID} ({docTitle})"
              .format(term=query, docID=docID, docTitle=doc_id_mapping[docID]))


def intersect(p1, p2):
    '''Intersects p1 postings lists and returns the inverted_index_by_query.'''
    answer = []
    # code to find inverted_index_by_query goes here
    """
    pythonic way :answer = [x for x in p1.values() if x in p2.values()][0]
    """

    docID1 = 0
    docID2 = 0
    if len(p1) > 0 and len(p2) > 0:
        while docID1 < len(p1) and docID2 < len(p2):
            if p1[docID1] == p2[docID2]:
                answer.append(p1[docID1])
                docID1 += 1
                docID2 += 1
            else:
                if p1[docID1] < p2[docID2]:
                    docID1 += 1
                else:
                    docID2 += 1
    return answer


def process_conjunctive_query(query, inverted_index, doc_id_mapping):
    '''
    Calls the inverted_index_by_query algorithm and displays the inverted_index_by_query (with
    the corresponding document names) of two posting lists for a query
    connected by an 'AND'.
    '''

    # split user query and remove 'AND'
    query_terms = [t.strip() for t in query.split("AND")]
    if len(query_terms) == 2:
        term1, term2 = query_terms[0], query_terms[1]
        p1, p2 = inverted_index[term1], inverted_index[term2]
        results = intersect(p1, p2)
        for docID in results:
            print("Term '{term1}' AND '{term2}' found in document {docID} ({docTitle})".format(
                term1=term1, term2=term2, docID=docID, docTitle=doc_id_mapping[docID]))
    else:
        print("The number of query should be two or query doesn't contain AND operator.")
        return


# Start of the main program.
if __name__ == "__main__":
    # Dictionary for the inverted index.
    inverted_index, doc_name_mapping = make_inverted_index("files")

    # Get user input.
    query = input("Query: ")
    # A conjunctive query.
    if "AND" in query:
        process_conjunctive_query(query, inverted_index, doc_name_mapping)
    # Simple query with one term.
    else:
        process_simple_query(query, inverted_index, doc_name_mapping)
