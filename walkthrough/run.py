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
    for doc in enumerate(files_data):
        doc_id_mapping[doc[0]] = doc[1]

    # The entire text for each document is now saved in 'files_data'.
    # Now tokenize each document using 'tokenizer.tokenize'
    # Don't forget to use .lower() function before tokenizing the text

    # Code to create inverted index goes here

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

    # Get user input.
    query = input("Query: ")

    # A conjunctive query.
    if "AND" in query:
        process_conjunctive_query(query, inverted_index, doc_name_mapping)
    # Simple query with one term.
    else:
        process_simple_query(query, inverted_index, doc_name_mapping)
