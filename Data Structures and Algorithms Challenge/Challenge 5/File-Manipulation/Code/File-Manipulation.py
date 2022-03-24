# Import libraries

import os
import glob


# SEARCH FUNCTION
def searchFile(path, criteria):
    
    result = []

    # File Extension based search
    if criteria[0] == ".":
        directory = path
        pathname = directory + "/**/*" + criteria
        result = glob.glob(pathname, recursive=True)
        
    # File Name based search
    else:
        for root, dir, files in os.walk(path):
            if criteria in files:
                result.append(os.path.join(root, criteria))

    return result
    
    
# SORT FUNCTION
def sortFile(path, criteria):
    
    result = []
    
    # File Name based sort
    if criteria == 1:
        list_of_files = filter(os.path.isfile, glob.glob(path + '/**/*', recursive=True))
        result = sorted(list_of_files)
        
    # File Size based sort
    elif criteria == 2:
        list_of_files = filter(os.path.isfile, glob.glob(path + '/**/*', recursive=True))
        result = sorted(list_of_files, key = lambda x: os.stat(x).st_size)
        
    # File Time based sort
    elif criteria == 3:
        list_of_files = filter(os.path.isfile, glob.glob(path + '/**/*', recursive=True))
        result = sorted(list_of_files, key = os.path.getmtime)

    return result
    
    
# DRIVER FUNCTION
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
            
        print()
        print("-----Search Result-----")
        if len(result) > 0:
            for i in result:
                print(i)
        else:
            print("The search process cannot be accomplished !")


    # SORT FILE PROCESSING
    elif option == 2:
        print("Do you want to sort by file name, file size or file time?")
        print("1 - Sort by File Name")
        print("2 - Sort by File Size")
        print("3 - Sort by File Time")
        criteria = int(input("Choose one of the above 3 options: "))
        
        result = sortFile(path, criteria)
            
        print()
        print("-----Sort Result-----")
        for i in result:
            print(i)
        
        
    elif option == 2:
        segregateFile()
        
    elif option == 2:
        mergeFile()

    else:
        print("There is no such option")
        

# DRIVER FUNCTION CALL
if __name__ == "__main__":
    main()