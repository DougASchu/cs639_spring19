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
      mr.emit_intermediate((i, k), value)
  if matrix_name == 'b':
    for k in range(5):
      mr.emit_intermediate((k, j), value)
    

# Implement the REDUCE function
def reducer(key, list_of_values):
    # YOUR CODE GOES HERE
    i = key[0]
    k = key[1]
    total = 0
    # This is needed to correctly match values for multiplication, thus this program only works for 5x5 matricies
    matrix_size = 5
    for index in range(matrix_size): 
      total += (list_of_values[index] * list_of_values[(index + matrix_size)])
    final_matrix_entry = [i, k, total]
    mr.emit(final_matrix_entry)

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
