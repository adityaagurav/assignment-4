file1 = open('assn.txt','r')
reading_file = file1.read()
print(reading_file)
file1.close()

try:
    file2 = open('sample.txt', 'r')
    reading_file2 = file2.read()
    print(reading_file2)
    file2.close()
except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")