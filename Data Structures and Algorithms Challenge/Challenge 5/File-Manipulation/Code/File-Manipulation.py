# Import libraries

import os
import glob
import shutil
import pyinputplus as pyip

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
    
    
# SEGREGATE FUNCTION
def segregateFile(path):
    
    # List of all files in the path
    list_of_files = os.listdir(path)
    
    for file in list_of_files:
    
        # Get file name and extension
        name, extension = os.path.splitext(file)
        # Ignore the . in file extension
        extension = extension[1:]
        
        # If file has no extension, continue
        if extension == '':
            continue
        
        # If there exists a folder for the extension, move the file from path to that specific folder
        if os.path.exists(path + '/' + extension):
            shutil.move(path + '/' + file, path + '/' + extension + '/' + file)
            
        # If the folder does not exist, create a folder named based on extension and then copy files from path to the new folder
        else:
            os.makedirs(path + '/' + extension)
            shutil.move(path + '/' + file, path + '/' + extension + '/' + file)
            

def mergeFile(path, extension):

    list_of_files = [i for i in glob.glob('*' + extension)]
        
    
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
    option = pyip.inputInt(prompt="Choose one of the above 4 options: ", greaterThan=0, lessThan=5)
    path = pyip.inputStr(prompt="Enter the path where you want to perform the above operation: ")
    
    # SEARCH FILE PROCESSING
    if option == 1:
        print("Do you want to search by extension or by file name?")
        print("1 - Search by Extension")
        print("2 - Search by File Name")
        criteria = pyip.inputInt(prompt="Choose one of the above 2 options: ", greaterThan=0, lessThan=3)
        
        if criteria == 1:
            extension = pyip.inputStr(prompt="Enter the file extension: ")
            result = searchFile(path, extension)
            
        elif criteria == 2:
            searchFileName = pyip.inputStr(prompt="Enter the name of the file to be searched: ")
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
        criteria = pyip.inputInt(prompt="Choose one of the above 3 options: ", greaterThan=0, lessThan=4)
        
        result = sortFile(path, criteria)
            
        print()
        print("-----Sort Result-----")
        for i in result:
            print(i)
        
        
    # SEGREGATE FILE PROCESSING
    elif option == 3:
        segregateFile(path)
        
        
    # MERGE FILE PROCESSING
    elif option == 4:
        extension = input("Enter the extension for merging those files: ")
        result = mergeFile(path, extension)

    # NO OPTION
    else:
        print("There is no such option")
        

# DRIVER FUNCTION CALL
if __name__ == "__main__":
    main()