# File Creation
try:
    with open("my_file.txt", 'w') as file:
        file.write("I am a PLP python student.\n")
        file.write("And  ilove coding inn python: 42\n")
        file.write("Thank you PLP.\n")
    print("File created and initial content written successfully.")
except (FileNotFoundError, PermissionError) as e:
    print(f"Error creating or writing to file: {e}")
finally:
    print("File creation and writing process finished.")

#Reading and Display
try:
    with open("my_file.txt", 'r') as file:
        content = file.read()
        print("\nContent of 'my_file.txt':")
        print(content)
except FileNotFoundError:
    print("Error: The file does not exist.")
except PermissionError:
    print("Error: You do not have permission to read the file.")
finally:
    print("File reading process finished.")

# File Appending
try:
    with open("my_file.txt", 'a') as file:
        file.write("Appending a new line.\n")
        file.write("Adding another line with a number: 99\n")
        file.write("And one more line to finish.\n")
    print("Additional lines appended successfully.")
except (FileNotFoundError, PermissionError) as e:
    print(f"Error appending to file: {e}")
finally:
    print("File appending process finished.")
