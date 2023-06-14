import shutil

shutil.copy2('text.txt', 'copy.txt')  #sourse,destination

with open('copy.txt') as file:
    print(file.read())