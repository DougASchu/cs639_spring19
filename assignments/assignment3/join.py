import MapReduce
import sys

"""
JOIN in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

# Douglas Schumacher, CS 639, March 2019

# Implement the MAP function
def mapper(record):
    key = record[1]
    mr.emit_intermediate(key, record)

# Implement the REDUCE function
def reducer(key, list_of_values):
  # YOUR CODE GOES HERE
  order_record = []
  # Find the order record
  for record in list_of_values:
    if record[0] == 'order':
      order_record = record
  # Put together matches of order and line item records
  for record in list_of_values:
      if record != order_record:
        mr.emit(order_record + record)
  
# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
