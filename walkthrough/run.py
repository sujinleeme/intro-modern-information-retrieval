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
    files_names = sorted([x for x in files_data.keys()],reverse=False)
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
    print(inverted_index)
    return inverted_index, doc_id_mapping


def process_simple_query(query, inverted_index, doc_id_mapping):
    '''Returns the postings list (and the corresponding document names)
    for a one-word query.'''

    # Code to process a one-word query goes here
    # Nothing needs to be returned. Simply print the results.


def intersect(p1, p2):
    '''Intersects two postings lists and returns the intersection.'''

    answer = []

    # code to find intersection goes here

    return answer


def process_conjunctive_query(query, inverted_index, doc_id_mapping):
    '''
    Calls the intersection algorithm and displays the intersection (with
    the corresponding document names) of two posting lists for a query
    connected by an 'AND'.
    '''

    # split user query and remove 'AND'
    query_terms = [t.strip() for t in query.split("AND")]

    # Code to process conjunctive query goes here.
    # You will need to call the intersect() function.
    # No need to return anything. Simply print the results.


# Start of the main program.
if __name__ == "__main__":
    # Dictionary for the inverted index.
    inverted_index, doc_name_mapping = make_inverted_index("files")
    # cprint(inverted_index, doc_name_mapping)
    # Get user input.
    # query = input("Query: ")

    # A conjunctive query.
    # if "AND" in query:
    #    process_conjunctive_query(query, inverted_index, doc_name_mapping)
    # Simple query with one term.
    # else:
    #   process_simple_query(query, inverted_index, doc_name_mapping)
