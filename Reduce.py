# reduce() = apply a function to an iterable and reduce it to a single cumulative value.
#            performs function on first two elements and repeats process until 1 value remains
#
# reduce(function, iterable)

import functools

letters = ["B", "H", "O", "L", "U"]

word = functools.reduce(lambda x,y : x+y  ,letters)
print(word)


# factorial Code
factorial = [4,3,2,1]
result = functools.reduce( lambda x,y : x*y  ,factorial)

print(result)
