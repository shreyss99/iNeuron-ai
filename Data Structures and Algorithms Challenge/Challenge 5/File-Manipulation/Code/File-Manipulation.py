# Import libraries

import os
import glob


def main():

    # Print the menu
    print("Welcome to FILE MANIPULATION project")
    print()
    print("--------MENU-------")
    print("1 - Search a File")
    print("2 - Sort Files")
    print("3 - Segregate Files")
    print("4 - Merge Files")
    print()

    # Ask user for options and path
    option = int(input("Choose one of the above 4 options: "))
    path = input("Enter the path where you want to perform the above operation: ")
    
    # SEARCH FILE PROCESSING
    if option == 1:
        print("Do you want to search by extension or by file name?")
        print("1 - Search by Extension")
        print("2 - Search by File Name")
        criteria = int(input("Choose one of the above 4 options: "))
        
        if criteria == 1:
            extension = input("Enter the file extension: ")
            result = searchFile(path, extension)
            
        elif criteria == 2:
            searchFileName = input("Enter the name of the file to be searched: ")
            result = searchFile(path, searchFileName)





# Define the driver code

if __name__ == "__main__":
    main()