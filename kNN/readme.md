# Simple kNN classifier
* python3

This is a simple kNN classifier, which asks the user for a k and then assigns a class to new documents.

The documents are labeled in `train` folder either `spam`or `ham` . The first line of each document contains its class and the following lines contain the text of the document. For example,

```
Ham
Hi to all
Here is my problem. I’m trying to export this data to SQL database.
[…]
```

## How it works
* (a) Omit the stop words listed in `stopwords.txt `. 
* (b) Use the tf-idf weighting for the vector values.
* (c) Normalize the vectors to unit vectors. Save the
information about the class of a document while it is processed.
* (d) Write a method to calculate the Euclidean distance between two
document vectors.
* (e) The main program now should be able to take the number of next neighbors `k` when assigning the test set documents to a class. Then it should perform kNN classification with the given `k`.

# How to run
This program must be executed with three arguments: the folder
containing the training files; the test file; and k. 

```
$ python3 knn.py [test_folder] [test_file_1] [k_value]
```

For an example, run this command:
```
python3 knn.py train 00000.txt 6     
```

You should see output such as this:
```
train 00000.txt 6

Total:  354
Calculating Euclidean distance between the new document and the training documents ...
Assigned class: spam
Correct class assigned to new document! :-)
Nearest neighbours:
('02363.txt', 1.2739546396032875)
('02369.txt', 1.3155863471679343)
('02365.txt', 1.346646143125217)
('02361.txt', 1.348913430740501)
('02364.txt', 1.35717898843382)
('02367.txt', 1.3705387900369748)
Time duration: 0.02
```