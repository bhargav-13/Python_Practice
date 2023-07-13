#Type:->

print("type() function")
a = 13
print(f"{a} is from {type(a)}")

a = 13.11
print(f"{a} is from {type(a)}")


print()

print("range() function")
print("Using 1st method:")
for i in range(5):
    print(i, end=" ")
print()

print("Using 2nd method:")
for i in range(10,15):
    print(i, end=" ")
print()

print("Using 3rd method:")
for i in range(1,10,2):
    print(i, end=" ")
print()

print()

print("Base Conversion:-")
a = 69

print(bin(a))

print(oct(a))

b = hex(a)
print(hex(a))

print(int(b, 16))