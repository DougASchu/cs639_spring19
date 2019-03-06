import MapReduce
import sys

"""
Matrix Multiply in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

# Douglas Schumacher, CS 639, March 2019
# Implement the MAP function
def mapper(record):
  # YOUR CODE GOES HERE
  matrix_name = record[0]
  i = record[1]
  j = record[2]
  value = record[3]
  if matrix_name == 'a':
    for k in range(5):
      mr.emit_intermediate((i, k), (m, j, value))
  if matrix_name == 'b':
    for k in range(5):
      mr.emit_intermediate((j, k), (i, value)
    

# Implement the REDUCE function
def reducer(key, list_of_values):
    # YOUR CODE GOES HERE
    total = 0
    final_matrix_entry = []
    for entry1 in list_of_values:
      for entry2 in list_of_values:
        if entry2[1] == entry1[1]:
          total += entry2[1] * entry1[1]
    final_matrix_entry = [key[0], key[1], total]
    mr.emit(final_matrix_entry)

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
