#Given an integer, NN, print its first 1010 multiples. Each multiple N×iN×i (where 1≤i≤101≤i≤10) should be printed on a new line in the form: N x i=resultN x i=result.
# import sys

N = int(raw_input().strip())

count = 1
while count <= 10:
  result = count * N
  print N, "x", count, "=", result
  count += 1
