import os

# path = "C:\\Users\\bharg\\OneDrive\\Desktop\\test.txt"

# if os.path.exists(path):
#     print("that location exist!")
#     if os.path.isfile(path):
#         print("THAT IS A FILE!!")
# else:
#     print("that location doesn't exist!")

text = "\nYou can Write in this file"

with open('text.txt', 'a') as file:
    file.write(text)

try:
    with open('text.txt') as file:
        print(file.read())
except FileNotFoundError:
    print("file doesn't exist")
