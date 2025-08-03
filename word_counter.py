#taking input from the user about the filename
def get_filename():
    filename=input("Enter the file name from which you want to count the words")
    return filename

#function to try except if the file exists or not and if it doesnot exist we will directly close thep program with exit
def file_read(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        print("File does not exist")
        exit()

#function to count number of words
def count_words(content):
    words = content.split()
    count = len(words)
    return count

#main function
def main():
    filename=get_filename()
    content=file_read(filename)
    count=count_words(content)
    print(f"The total no of words is {count}")

