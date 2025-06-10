# assignment-4_1
we take user input and write to output.txt
with open('output.txt', 'w') as file:
    data = input("Enter some text: ")
    file.write(data + '\n')

we append additional data
with open('output.txt', 'a') as file:
    more_data = input("Enter additional text to append: ")
    file.write(more_data + '\n')

Read and display the final content
with open('output.txt', 'r') as file:
    content = file.read()
    print("Final content of output.txt:")
    print(content)

# assignment-4_2
This program demonstrates file writing, appending, and reading operations.
It takes user input and writes it to output.txt.
It then takes additional input and appends it to the same file.
Finally, it reads and displays the complete content of output.txt.
