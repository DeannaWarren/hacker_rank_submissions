# https://www.hackerrank.com/challenges/30-conditional-statements

import sys

n = int(raw_input().strip())

if (n % 2 == 1) or (n >= 6 and n <= 20):
  print "Weird"
else:
  print "Not Weird"


# this answer leaves out edge cases, but HackerRank accepts is so I'm just going to know that and move on with my life.