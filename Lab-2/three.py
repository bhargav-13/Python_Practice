#  1)Assignment operator

a = 10
b = 5

addition = a+b
sub = a-b

print(addition)
print(sub)

# Example:  (+ - * / % ** //)

# 2) Relational or Comparison Operators:
print(a>b)
print(b>a)

# Example:  (< > <= >= == !=)

# 3) Equality Operators:

print(a == b)
print(a != b)

# 4) Bitwise Operators:

print(b & a) #AND
print(a | b) #OR
print(a ^ b) #XOR
print(~a)    #NOT


# 5)Shift Operators:

print(a << 1)    # a = 10 binary=(0000 1010) one will be shifted to left (0001 0100)
print(a >> 1)   # a = 10 binary=(0000 1010) one will be shifted to right (0000 0101)

# 6) Assignment Operators:
a += 2
print(a)

# Example = (+= -= *= /= %= //= **=)

# 7) Ternary Operator (Conditional Operator):

result = "Even" if a % 2 == 0 else "Odd"

print(result)

# 8) Special Operators:
#     a)Identity Operators:

print(a is b)                    # compare memory location
print(a is not b)

#     b) Membership Operators:

list = [1,4,5,13]

print(13 in list)
print(50 in list)

# 9) logical operator
p = True
q = False

print(p and q)
print(p or q)

# 10) Operator Precedence:
result = 5 + 2 * 3

print(result)  # Output: 11
