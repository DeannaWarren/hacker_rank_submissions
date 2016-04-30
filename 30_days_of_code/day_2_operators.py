# https://www.hackerrank.com/challenges/30-operators
# Enter your code here. Read input from STDIN. Print output to STDOUT

meal_cost = float(raw_input())
tip_percent = float(raw_input())
tax_percent = float(raw_input())

tip_value = round(meal_cost * (tip_percent/100), 2)
tax_value = round(meal_cost * (tax_percent/100), 2)

total_cost = int(round(meal_cost + tip_value + tax_value))

print "The total meal cost is", total_cost, "dollars."