import MapReduce
import sys

"""
Friend Count in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line
# Douglas Schumacher, CS 639, March 2019

# Implement the MAP function
def mapper(record):
    # YOUR CODE GOES HERE
  name = record[0]
  mr.emit_intermediate(name, 1)

# Implement the REDUCE function
def reducer(key, list_of_values):
    # YOUR CODE GOES HERE
  friend_count = sum(list_of_values)
  mr.emit((key, friend_count))
# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
