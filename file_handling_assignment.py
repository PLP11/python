#This uses three function so as to make it simple .Each with try and except for errros.
#The create file (this will deal with writing mode for creating the text file).
#read file reading the file that has been written
#append file for appending
def create_file():
    try:
        # This Create a new text file named "my_file.txt" in write mode ('w').We use with
        with open("my_file.txt", "w") as f:
            # Write at least three lines of text to the file
            f.write("I think that python coding should be taught again.\n")
            f.write("This is my favorite number,070569\n")
            f.write("Is there any recording for cohort 4?__\n")
            #Using exception as it handles multiple types of errors
    except Exception as e:
        print("An error occurred while creating the file:", e)


def read_file():
    try:
        # Open "my_file.txt" in read mode ('r')
        with open("my_file.txt", "r") as f:
            # Read the contents of the file
            content = f.read()
            print("Content of my_file.txt:")
            print(content)
    except FileNotFoundError:
        print("File not found!")
    except PermissionError:
        print("Permission denied to read the file!")
    except Exception as e:
        print("An error occurred while reading the file:", e)


def append_to_file():
    try:
        # It Open "my_file.txt" in append mode ('a')
        with open("my_file.txt", "a") as f:
            # This Append three additional lines of text to the existing content
            f.write("This is a new line added through appending.\n")
            f.write("67890\n")
            f.write("Appending is fun!\n")
            #defines errors
    except FileNotFoundError:
        print("File not found!")
    except PermissionError:
        print("Permission denied to append to the file!")
    except Exception as e:
        print("An error occurred while appending to the file:", e)


if __name__ == "__main__":
    create_file()
    read_file()
    append_to_file()
