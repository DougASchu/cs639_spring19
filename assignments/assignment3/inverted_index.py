import MapReduce
import sys

"""
Inverted Index Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

# Douglas Schumacher, CS 639, March 2019
# Implement the MAP function
def mapper(record):
    docID = record[0]
    text = record[1]
    word_list = text.split()
    previous_words = []
    for word in word_list:
      if word not in previous_words:
            mr.emit_intermediate(word, docID)
            previous_words.append(word)

# Implement the REDUCE function
def reducer(key, list_of_values):
    docID_list = []
    for docID in list_of_values:
      if docID not in docID_list:
        docID_list.append(docID)
    mr.emit((key, docID_list))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
