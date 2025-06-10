with open('output.txt', 'w') as file:
    data = input("Enter some text: ")
    file.write(data + '\n')

with open('output.txt', 'a') as file:
    more_data = input("Enter additional text to append: ")
    file.write(more_data + '\n')
    
with open('output.txt', 'r') as file:
    content = file.read()
    print("Final content of output.txt:")
    print(content)