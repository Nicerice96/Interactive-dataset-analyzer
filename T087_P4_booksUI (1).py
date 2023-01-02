#Zarif Khan 101224172
#Aiden Hepburn 101220580
#Chen Chen 101235800
#Ben MetCalfe 101234641

#import for case1
import string

from T087_P1_load_data import book_category_dictionary
import T087_P2_add_remove_search_dataset 

#import for case2
import string
from T087_P1_load_data import book_category_dictionary  
from T087_P2_add_remove_search_dataset import get_books_by_rate
from T087_P2_add_remove_search_dataset import get_book_by_title
from T087_P2_add_remove_search_dataset import get_books_by_author

#import for case3
from T087_P2_add_remove_search_dataset import get_books_by_publisher #imported seperately for less complicated calls
from T087_P2_add_remove_search_dataset import get_books_by_category
from T087_P2_add_remove_search_dataset import get_all_categories_for_book_title
from T087_P1_load_data import book_category_dictionary

#import for case4
from T087_P1_load_data import book_category_dictionary
from T087_P3_sorting_fun import sort_books_title
from T087_P3_sorting_fun import sort_books_publisher
from T087_P3_sorting_fun import sort_books_author
from T087_P3_sorting_fun import sort_books_ascending_rate


def print_commands() -> str:
    
    """this function prints the available commands that the user can use
    
    >>>print_commands()
    
    1- L)oad Data 
2- A)dd book 
3- R)emove book 
4- G)et books
    T)itle   R)ate   A)uthor   P)ublisher   C)ategory
5- GCT) Get all categories for book Title 
6- S)ort books
    T)itle   R)ate   P)ublisher   A)uthor
7- Q)uit
    """
    
    print("The available commands are:\n"\
          "1- L)oad Data \n2- A)dd book \n3- R)emove book \n4- G)et books\n"\
          "    T)itle   R)ate   A)uthor   P)ublisher   C)ategory\n"\
          "5- GCT) Get all categories for book Title \n6- S)ort books\n"\
          "    T)itle   R)ate   P)ublisher   A)uthor\n"\
          "7- Q)uit")
    
    #command = (input("Please enter your command (Q to quit): "))
    #print(command.upper())
    
    return #command


def load_file(file:str) -> dict:
    
    """loads the user inputted file and directs the file to a prexsiting module that sorts the data from the file based on category"""
    
    
    
    return book_category_dictionary(file)


def user_interface(command:str):
    
    """The available commands are:
1- L)oad Data 
2- A)dd book 
3- R)emove book 
4- G)et books
    T)itle   R)ate   A)uthor   P)ublisher   C)ategory
5- GCT) Get all categories for book Title 
6- S)ort books
    T)itle   R)ate   P)ublisher   A)uthor
7- Q)uit
Please enter your command (Q to quit): L
L
Input file name: google_books_dataset.csv
{'Fiction': [{'title': "Antiques Roadkill: A Trash 'n' Treasures Mystery", 'author': 'Barbara Allan', 'rating': '3.3', 'publisher': 'Kensington Publishing Corp.', 'pages': '288', 'language': 'English'}, {'title': 'The Painted Man (The Demon Cycle. Book 1)', 'author': 'Peter V. Brett', 'rating': '4.5', 'publisher': 'HarperCollins UK', 'pages': '544', 'language': 'English'}, {'title': 'Edgedancer: From the Stormlight Archive', 'author': 'Brandon Sanderson', 'rating': '4.8', 'publisher': 'Tor Books', 'pages': '226', 'language': 'English'}, {'title': 'Sword of Destiny: Witcher 2: Tales of the Witcher', 'author': 'Andrzej Sapkowski', 'rating': '4.8', 'publisher': 'Hachette UK', 'pages': '400', 'language': 'English'}, {'title': 'After Anna', 'author': 'Alex Lake', 'rating': '4.1', 'publisher': 'HarperCollins UK', 'pages': '416', 'language': 'English'}, {'title': 'Little Girl Lost: A Lucy Black Thriller', 'author': 'Brian McGilloway', 'rating': '4', 'publisher': 'Harper Collins', 'pages': '336', 'language': 'English'}, .....}]}
Please enter your command (Q to quit): A
A
title of book you want to add: title
author of book you want to add: author
language of book you want to add: language
publisher of book you want to add: publisher
category of book you want to add: Fiction
rating of book you want to add: rating
pages of book you want to add: pages
The book has been added correctly
There was an error adding the book
There was an error adding the book
There was an error adding the book
There was an error adding the book
There was an error adding the book
There was an error adding the book
There was an error adding the book
There was an error adding the book
There was an error adding the book
There was an error adding the book
There was an error adding the book
There was an error adding the book
There was an error adding the book
There was an error adding the book
There was an error adding the book
There was an error adding the book
There was an error adding the book
There was an error adding the book
There was an error adding the book
There was an error adding the book
There was an error adding the book
There was an error adding the book
There was an error adding the book
There was an error adding the book
There was an error adding the book
{'Fiction': [{'title': "Antiques Roadkill: A Trash 'n' Treasures Mystery", 'author': 'Barbara Allan', 'rating': '3.3', 'publisher': 'Kensington Publishing Corp.', 'pages': '288', 'language': 'English'}, {'title': 'The Painted Man (The Demon Cycle. Book 1)', 'author': 'Peter V. Brett', 'rating': '4.5', .....}]}
Please enter your command (Q to quit): R
R
title of book you want to remove: In Dark Company: A Kate Burkholder Short Story
category of book you want to remove: Thrillers
The book has been removed correctly
Please enter your command (Q to quit): G
G
Get books command
The available commands are:
1- T)itle
2- R)ate
3- A)uthor
4- P)ublisher
-5 C)ategory
-6 Q)uit

Please enter a command (Q to quit): T
T
Enter name of the title: The Malady and Other Stories: An Andrzej Sapkowski Sampler
The book has been found
Please enter your command (Q to quit): Q
Q
Program ended
"""
    command = ''
    command_list = ['L', 'A', 'R', 'G', 'T', 'P', 'C', 'GCT', 'S', 'Q']
    dictionary = ""
    file1 = 0    
    print_commands()
    
    #While input is not Q
    while command.upper() != 'Q':
        
        command = (input("Please enter your command (Q to quit): "))
        print(command.upper())
        
        #Wrong input
        if command.upper() not in command_list:
            print("No such command")
      
        #Load File
        elif command.upper() == "L":
            file1 = load_file(input("Input file name: "))
            print(file1)
            dictionary = file1        
        
        
        if command.upper() == 'A':
            if file1 == 0:
                print("No file loaded")
            
            else:   
                title = input("title of book you want to add: ")
                author = input("author of book you want to add: ")
                language = input("language of book you want to add: ")
                publisher = input("publisher of book you want to add: ")
                category = input("category of book you want to add: ")
                rating = input("rating of book you want to add: ")
                pages = input ("pages of book you want to add: ")
                
                book_info = (title, author, language, publisher, category, rating, pages)
            
                title, author, language, publisher, category, rating, pages = book_info
                
                T087_P2_add_remove_search_dataset.add_book(dictionary, book_info)
                
                print (dictionary)                
                
        
        elif command.upper() == 'R':
            if file1 == 0:
                print("No file loaded") 
                
            else:
                title = input("title of book you want to remove: ")
                category = input("category of book you want to remove: ")
                
                T087_P2_add_remove_search_dataset.remove_book(dictionary, title, category)
                
                
        elif command.upper() == 'G':
            
            if file1 == 0:
                
                print("No file loaded")  
                
            else:
                
                print("Get books command")
                print("The available commands are:\n"\
                      "1- T)itle\n2- R)ate\n3- A)uthor\n4- P)ublisher\n-5 C)ategory\n-6 Q)uit\n")                
                command = (input("Please enter a command (Q to quit): "))
                print(command.upper())
                
                #Title
                if command.upper() == "T":
                    title = input("Enter name of the title: ")
                    get_book_by_title(dictionary, title)
                    
                #Rating
                elif command.upper() == "R":
                    rating = int(input("Enter the rating of the books: "))
                    get_books_by_rate(dictionary, rating)
                    
                #Author
                elif command.upper() == "A":
                    author = input("Enter name of the author: ")
                    get_books_by_author(dictionary, author)
                    
                #Publisher
                elif command.upper() == "P":
                    publisher = input("Enter name of the publisher: ")
                    get_books_by_publisher(dictionary, publisher)
                        
                #Category
                elif command.upper() == "C":
                    category = input("Enter name of the category: ")
                    get_books_by_category(dictionary, category)                
                    
                #Quit
                elif command.upper() == "Q":
                    break  
                
                #No command
                else:
                    print("No such command")
                          
                                 
        elif command.upper() == 'GCT':
            if file1 == 0:
                print("No file loaded")  
            else:
                title = input("Enter name of the title: ")
                get_all_categories_for_book_title(dictionary, title)
                
        elif command.upper() == 'S':
            if file1 == 0:
                print("No file loaded")
            else:
                print("Sort books command")
                print("The available commands are:\n"\
                      "1- T)itle\n2- R)ate\n3- P)ublisher\n4- A)uthor\n5- Q)uit\n")                
                command = (input("Please enter a command (Q to quit): "))
                print(command.upper()) 
                
                if command.upper() == 'T':
                    
                    sort_books_title(dictionary)   
                    
                elif command.upper() == 'R':
                    
                    sort_books_ascending_rate(dictionary)  
                    
                elif command.upper() == 'P':
                    
                    sort_books_publisher(dictionary)  
                    
                elif command.upper() == 'A':
                    
                    sort_books_author(dictionary)  
                    
                elif command.upper() == 'Q':
                    break                    
                else:
                    print('No such command')
                
    print("Program ended")           
    return

user_interface('command')