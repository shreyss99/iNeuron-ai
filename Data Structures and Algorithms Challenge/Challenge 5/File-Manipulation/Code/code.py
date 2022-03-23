import os
import glob

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


def segregateFile():
    pass


def main():
    print("Welcome to FILE MANIPULATION project")
    print()
    print("--------MENU-------")
    print("1 - Search a File")
    print("2 - Sort Files")
    print("3 - Segregate Files")
    print("4 - Merge Files")
    print()
    option = int(input("Choose one of the above 4 options: "))
    path = input("Enter the path where you want to perform the above operation: ")

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
        if len(result) > 0:
            for i in result:
                print(i)
        else:
            print("The search process cannot be accomplished !")
        
        
    elif option == 2:
        sortFile()
        
    elif option == 2:
        segregateFile()
        
    elif option == 2:
        mergeFile()

    else:
        print("There is no such option")

if __name__ == "__main__":
    main()