import MapReduce
import sys

"""
Assymetric Relationships in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line
# Douglas Schumacher, CS 639, March 2019

# Implement the MAP function
def mapper(record):
  # YOUR CODE GOES HERE
  name1 = record[0]
  name2 = record[1]
  mr.emit_intermediate(min(name1, name2), [1, name1, name2])

# Implement the REDUCE function
def reducer(key, list_of_values):
  # YOUR CODE GOES HERE
  list_of_assym = list_of_values
  for relationship in list_of_values:
    for relation in list_of_values:
      if relation == [1, relationship[2], relationship[1]]:
        list_of_assym.remove(relationship)
        list_of_assym.remove(relation)

  for relation in list_of_assym:
    mr.emit([relation[2], relation[1]])
# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
