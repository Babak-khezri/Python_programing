from colorama import Fore ,init
from click import getchar
from os import system
init(convert=True)
print(Fore.CYAN + "Add the list elements : ")
lst = list(map(int,input("").split()))
def show():
    system('cls')
    print("1_Show normal list : ")
    print("2_Show sorted list : ")
    while True:
        ch = getchar()
        system('cls')
        if int(ch) == 1:
            print("Your list : ",end="")
            for i in lst:
                print(i,end = " ")
            print(Fore.YELLOW + "\nAny key to get back : ...")
            back = getchar()
            Menu()
        if int(ch) == 2:
            system('cls')
            copy = sorted(lst)
            print("Your list : ",end="")
            for i in copy:
                print(i,end = " ")
            print(Fore.YELLOW + "\nAny key to get back : ...")
            back = getchar()
            Menu()
def add_to():
    system('cls')
    print("1_Add to the first : ")
    print("2_Add to the end  : ")
    while True:
        ch = getchar()
        if int(ch) == 1:
            system('cls')
            add = int(input("Enter the element : "))
            lst.insert(0,add)
            Menu()
        if int(ch) == 2:
            system('cls')
            add = int(input("Enter the element : "))
            lst.append(add)
            Menu()
def Menu():
    system('cls')
    print(Fore.BLUE + "1_Show the list : ")
    print(Fore.BLUE + "2_Add to list : ")
    print(Fore.BLUE + "3_Delete from list : ")
    print(Fore.BLUE + "4_Search for Element : ")
    print(Fore.GREEN + "")
    while True:
        choice = getchar()
        if int(choice) == 1:
            show()
        if int(choice) == 2:
            add_to()
        if int(choice) == 3:
            Delete()
        if int(choice) == 4:
            search()
def Delete():
    system('cls')
    print("1_remove by name : ")
    print("2_remove by Position : ")
    while True:
        ch = getchar()
        if int(ch) == 1:
            while True:
                system('cls')
                remove = input("Enter the name of element : ")
                if int(remove) not in lst:
                    print("The element is not in list.")
                    continue
                lst.remove(int(remove))
                Menu()
        if int(ch) == 2:
            while True:
                system('cls')
                remove = input("Enter the name of element : ")
                if int(remove) not in lst:
                    print("The element is not in list.")
                    continue
                lst.pop(int(remove))
                Menu()
def search():
    system('cls')
    sear = int(input("Enter the element : "))
    if sear not in lst:
        print("The element is not exist ! ")
        print(Fore.YELLOW + "\nAny key to get back : ...")
        back = getchar()
        Menu()
    else:
        result = []
        find = []
        find.extend(lst)
        count = lst.count(sear)
        print("we find {} ".format(count))
        for i in range(count):
            result.append(find.index(sear)+1)
            find[find.index(sear)] = -100
        print("The element < {} > is in places ".format(sear),end="")
        print(result)
        print(Fore.YELLOW + "\nAny key to get back : ...")
        back = getchar()
        Menu()
Menu()