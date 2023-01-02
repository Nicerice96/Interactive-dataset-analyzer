#T087 
#Aiden Hepburn 101220580
#Zarif Khan 101224172
#Ben MetCalfe 101234641
#Chen Chen 101235800

#imports 

import T087_P1_load_data

book_dictionary = T087_P1_load_data.book_category_dictionary(r"C:\Users\Zarif\Downloads\google_books_dataset_THEGOODONE.csv")

book_test1 = T087_P1_load_data.book_category_dictionary(r"C:\Users\Zarif\Desktop\test_one.csv")
book_test2 = T087_P1_load_data.book_category_dictionary(r"C:\Users\Zarif\Desktop\test_two.csv")
book_test3 = T087_P1_load_data.book_category_dictionary(r"C:\Users\Zarif\Desktop\test_three.csv")
book_test4 = T087_P1_load_data.book_category_dictionary(r"C:\Users\Zarif\Desktop\test_four.csv")
book_test5 = T087_P1_load_data.book_category_dictionary(r"C:\Users\Zarif\Desktop\test_five.csv")
book_test6 = T087_P1_load_data.book_category_dictionary(r"C:\Users\Zarif\Desktop\test_six.csv")



#Check_Equal Function 

def check_equal(description: str, outcome, expected) -> None:
    """
    Print a "passed" message if outcome and expected have same type and
    are equal (as determined by the == operator); otherwise, print a 
    "fail" message.
    
    Parameter "description" should provide information that will help us
    interpret the test results; e.g., the call expression that yields
    outcome.
    
    Parameters "outcome" and "expected" are typically the actual value returned
    by a call expression and the value we expect a correct implementation
    of the function to return, respectively. Both parameters must have the same
    type, which must be a type for which == is used to determine if two values
    are equal. Don't use this function to check if floats, lists of floats,
    tuples of floats, etc. are equal. 
    """
    outcome_type = type(outcome)
    expected_type = type(expected)
    if outcome_type != expected_type:
        
        # The format methods is explained on pages 119-122 of 
        # 'Practical Programming', 3rd ed.
        
        print("{0} FAILED: expected ({1}) has type {2}, " \
              "but outcome ({3}) has type {4}".
              format(description, expected, str(expected_type).strip('<class> '), 
                      outcome, str(outcome_type).strip('<class> ')))
    elif outcome != expected:
        print("{0} FAILED: expected {1}, got {2}".
              format(description, expected, outcome))
        print("------")
        return False
    else:
        print("{0} PASSED".format(description))
        print("------")
        return True


# Function 1 (Zarif Khan 101224172)

def add_book (dictionary:dict(), book_info:tuple()) -> dict():
    
    
    """
    >>>get_all_categories_for_book_title(book_dictionary, "Antiques Con")
    [{
    
    """
    
    

    title, author, language, publisher, category, rating, pages = book_info
    
    for key in dictionary:
        if key == category:
            dicc = {"title":title, "author":author, "language":language, "publisher":publisher, "rating":rating, "pages":pages}
            dictionary[key].append(dicc)
            print ("The book has been added correctly")
        elif key != category: 
            print ("There was an error adding the book")            
            
    return dictionary


#Function 2 (Chen Chen 101235800)

def remove_book(dictionary:dict,title:str,category:str)->dict:
    #The function has three input parameters, (1) the dictionary from where the book must be removed, (2) the title of the book and (3) the category. The function returns the updated dictionary and prints a messagestating, “The book has been removed correctly” or “There was an error removing the book. Book not found.”    
    
    testify = False
    for i in dictionary.get(category):
        if i.get("title") == title:
            dictionary.get(category).remove(i)
            print("The book has been removed correctly")
            testify = True

    if testify == False:
        print("There was an error removing the book. Book not found.")
    return dictionary
    
#Function 3 (Aiden Hepburn 101220580)

def get_books_by_category(dictionary: dict, category: str) -> dict():

    number_books = 0
    count = 0

    for x in dict.keys(dictionary):

        if x == category:

            for n in dictionary[category]: # Get the number of books in the list
                number_books += 1

            print("The category", category, "has", number_books, " books. This is the list of books:")
            print()

            number_books = 0 #Reset the book counter to 0 for the book list

            for n in dictionary[category]:

                dictionary_category = dictionary[category]

                book_info = dictionary_category[count]

                title = book_info['title']

                author = book_info['author']

                number_books += 1

                print("Book", number_books, ":", title, "by", author)

                print()

                count += 1       

    return number_books


#Funtion 4 (Ben MetCalfe 101234641)
def get_books_by_rate(dictionary:dict, rate:int):
    """
    This function takes a dictionary and a value. The value being the rating of a book within the dictionary. The function reads the dictionary values (the book information) for the rating.
    If the rating value is greater than the desired value but less than value+1 it is added to a list and counted. The amount of books between the ratings is recorded and printed and the list of all the 
    books is printed in the desire format.
    Ex

    get_books_by_rate(book_dictionary, 3)
    
    There are 8 books whos rate is between 3 and 4. This is the list of books:
    Book 1 : Antiques Roadkill: A Trash 'n' Treasures Mystery by Barbara Allan
    Book 2 : Bring Me Back by B A Paris
    Book 3 : Mrs. Pollifax Unveiled by Dorothy Gilman
    Book 4 : How to Understand Business Finance: Edition 2 by Bob Cinnamon
    Book 5 : The Secrets of Saving and Investing with Alvin Hall: Simple Strategies to Make Your Money Go Further by Alvin Hall
    Book 6 : Freakonomics Rev Ed: A Rogue Economist Explores the Hidden Side of Everything by Steven D. Levitt
    Book 7 : The Infinite Game by Simon Sinek
    Book 8 : Selling 101: What Every Successful Sales Professional Needs to Know by Zig Ziglar

    """
    hi_rate=str(rate+1) #max rating to read
    rate=str(rate) #min rating to read
    list_of_books=[]
    no_repeats=[]
    already_in = set()
    
    for books_list in book_dictionary.values(): #for all the books in the dictionary
        for i in range(len(books_list)): #for elements in the books
            if rate<= books_list[i]['rating']<hi_rate: #if the element 'rating' is between the max and min values
                list_of_books.append(books_list[i])  #then put the book into our list oif books with y rating
            
    #removing duplicates           
    for dicts in list_of_books: #for the books in the list
        t = tuple(dicts.items()) #changes the info of the books into tuples
        if t not in already_in: #if the info isnt in our set (sets have no repeats)
            already_in.add(t)  
            no_repeats.append(dicts) #then add info to our list
            
    length=str(len(no_repeats)) # the amount of books within the rating
    print("There are " +length+ " books who's rate is between " +rate+ " and " +hi_rate+ ". This is the list of books:")
    
    counter = 1
    while counter < len(no_repeats): #while our counter is less than the amount of books, do below
        for items in no_repeats: #for all the items in our to-be-printed list
            print ("Book", counter, ": "+items['title']+ " by " +items['author']) #print the book# the item that associates with the title and the item associated with the author
            counter+=1
    
    return length





#Function 5 (Chen Chen 101235800) 

def get_book_by_title(dictionary:dict,title:str)->bool:
    #Use the function design recipe to develop a function named get_books_by_rate. The function has two input parameters, the dictionary where the data is stored and a positive integer argument which is the rate. The function returns the number of books.
    have_book = False
    for i in list(dictionary.values()):
        for o in i:
            if o.get("title") == title:
                have_book = True
    if have_book == False:
        print("The book has NOT been found")
    else:
        print("The book has been found")
    return have_book


        
        
#Function 6 (Aiden Hepburn 101220580)
def get_books_by_author(dictionary: dict, author:str) -> int:

    number_books = 0
    count = 0
    a = 0
    set_two = set()
    print("The author", author, "has published the following books:")
    print()

    for category in dictionary:
        dictionary_category = dictionary[category]
        count = 0

        for item in dictionary_category:
            information = dictionary_category[count]
            count += 1

            if information['author'] == author:
                title = information.get('title')
                rating = information['rating']

                if title not in set_two:
                    number_books += 1
                    print("Book", number_books, ":", title, ", rate:", rating)
                    print()
                    set_two.add(title)

    return number_books


         
#Function 7 (Ben MetCalfe 101234641)

def get_books_by_publisher(dictionary:dict, publisher:str):
    
    """
    This function takes a dictionary and a string. The string being a publisher who published books within the dictionary. The fuction reads the dictionarys values (book info) and if the publisher
    for a book matches the inputed publisher, thats book is added to a list then printed or formatted. The publishger is noted and printed as a stametnt aswell

    Ex
    get_books_by_publisher(book_dictionary, 'Marvel Entertainment')
    The publisher Marvel Entertainment has published the following books:
    Book 1 : Deadpool Kills the Marvel Universe by Cullen Bunn
    Book 2 : Ultimate Spider-Man Vol. 11: Carnage by Brian Michael Bendis
    Book 3 : Immortal Hulk Vol. 1: Or Is He Both? by Al Ewing
    Book 4 : Venomized by Cullen Bunn
    Book 5 : Spider-Man: Anti-Venom by Dan Slott
    Book 6 : Spider-Verse: Volume 1 by Dan Slott
    
    """
    list_of_books2=[]
    no_repeats2=[]
    already_in2 = set()
    
    for books_list in book_dictionary.values(): #for the books in our dictionary
        for i in range(len(books_list)):  #for elements in the books
            if books_list[i]['publisher']==publisher: #if the elemnt associated with publisher is the amae as our inputed publisher
                list_of_books2.append(books_list[i]) #then add it to our list
            
    #removing duplicates           
    for dicts in list_of_books2: #For the books in the new list
        t = tuple(dicts.items()) #changes the info of the books into tuples
        if t not in already_in2: #if the info isnt in our set (sets have no repeats)
            already_in2.add(t)
            no_repeats2.append(dicts)  #then add info to our list
            
    print("The publisher "+publisher+ " has published the following books:") 
    


            
    counter2 = 1
    while counter2 < len(no_repeats2): #While our counter is less than the amount of books published, do below
        for items in no_repeats2: # for the values in our list
            print ("Book", counter2, ": "+items['title']+ " by " +items['author']) #print the book# the item associated with the title and the item associated with the author
            counter2 += 1
            
    length2 = len(no_repeats2)

    return length2




#Function 8 (Zarif Khan 101224172)

def get_all_categories_for_book_title (dictionary: dict(), title: str) -> int:
    
    """this function returns the categories that a book is listed under
    
    >>>get_all_categories_for_book_title(book_dictionary, "Homecoming (A Chloe Fine Psychological Suspense Mystery Book 5)")
    2
    
    >>>get_all_categories_for_book_title(book_dictionary, "Edgedancer: From the Stormlight Archive")
    2
    
    >>>get_all_categories_for_book_title(book_dictionary, "Antiques Roadkill: A Trash 'n' Treasures Mystery")
    3

    """
    
    print ("The book title", title, "belongs to the following categories")
    
    set_one = set()
    counter = 0
    num_books = 0
    for i in book_dictionary:
        for j in dictionary[i]:
            for k in j:
                if j[k]== title:
                    category = i
                    set_one.add(category)
        
    for i in set_one:
        num_books += 1
        counter += 1
        print ("Category", counter, ":", i)
        
    return num_books
#----------------------------------------------------------------------------------------------------------------------------------------

#TESTING
                
# Function 1 test
    
def add_book_test(description: str, outcome, expected) -> None:
    """
    Returns None. The functions prints pass or failed depending on the outcome of the return when comparing the expected value to the outcome
    >>> add_book_test("Add books test 3:", add_book(book_dictionary, NEW_BOOK_THREE), book_dictionary)
    The book has been added correctly
    Add books test 3: PASSED
    """
    
    global test
    global passed
    global failed
     
    value = check_equal(description, outcome, expected)
    test += 1
    if value == True:
        passed += 1
    else:
        failed += 1    
        
        
#Function 2 Test

def remove_book_test(description: str, outcome, expected) -> None:
    global test
    global passed
    global failed
     
    value = check_equal(description, outcome, expected)
    test += 1
    if value == True:
        passed += 1
    else:
        failed += 1  


        
#Function 3 Test  

def get_books_by_category_test(description: str, outcome, expected) -> None:
    global test
    global passed
    global failed
     
    value = check_equal(description, outcome, expected)
    test += 1
    if value == True:
        passed += 1
    else:
        failed += 1  

#Function 4 Test

def get_books_by_rate_test(description: str, outcome, expected) -> None:
    global test
    global passed
    global failed
     
    value = check_equal(description, outcome, expected)
    test += 1
    if value == True:
        passed += 1
    else:
        failed += 1  
        
#Function 5 Test

def get_book_by_title_test(description: str, outcome, expected) -> None:
    global test
    global passed
    global failed
     
    value = check_equal(description, outcome, expected)
    test += 1
    if value == True:
        passed += 1
    else:
        failed += 1  

        
        
#Function 6 Test

def get_books_by_author_test(description: str, outcome, expected) -> None:
    global test
    global passed
    global failed
    
    value = check_equal(description, outcome, expected)
    test += 1
    if value == True:
        passed += 1
    else:
        failed += 1
        
        
#Function 7 Test
        
def get_books_by_publisher_test(description: str, outcome, expected) -> None:
    global test
    global passed
    global failed
    
    value = check_equal(description, outcome, expected)
    test += 1
    if value == True:
        passed += 1
    else:
        failed += 1
        
#Function 8 Test

def categories_for_book_title_test(description: str, outcome, expected) -> None:
    """
    Returns None. The functions prints pass or failed depending on the outcome of the return when comparing the expected value to the outcome
    >>> categories_for_book_title_test("Categories for book title test 1:", 3,get_all_categories_for_book_title(book_dictionary, "Antiques Con"))
    Categories for book title test 3: PASSED
    """
    
    global test
    global passed
    global failed
    
    value = check_equal(description, outcome, expected)
    test += 1
    if value == True:
        passed += 1
    else:
        failed += 1

#----------------------------------------------------------------------------------------------------------------------------------------
#MainScript


if __name__ == "__main__":
    
    
    total_passed = 0
    #Function 1 Test Calls
    
    #Set the testing variables to 0 to begin
    test = 0
    passed = 0
    failed = 0
    
    #Testing for categories for a book title
    
    #Books being added
    NEW_BOOK_ONE = ("Harry Potter and the Sorcerers Stone", "J.K Rowling", "English", "Bloomsbury", "Fiction", "4.5", "223")
    NEW_BOOK_TWO = ("Never Let Me Go", "Kazuo Ishiguro", "English", "Faber and Faber", "Fiction", "3.8", "288")
    NEW_BOOK_THREE = ("The Silence of the Lambs", "Thomas Harris", "English", "St. Martins Press", "Thrillers", "4.2", "388")
    
    #Testing for a book added
    add_book_test("Add books test 1:", add_book(book_dictionary, NEW_BOOK_ONE), book_test1)
    add_book_test("Add books test 2:", add_book(book_dictionary, NEW_BOOK_TWO), book_test2)
    add_book_test("Add books test 3:", add_book(book_dictionary, NEW_BOOK_THREE), book_test3)
    
    total_passed += passed
    
    print("\nTotal Tests:", test, "\nTests Passed:", passed, "\nTests Failed:", failed)
    print()
    
    #Set the testing variables to 0 to begin
    test = 0
    passed = 0
    failed = 0    
 
    
    #Function 2 Test Calls
    print ("Function 2 Test Calls")
    print ("remove_book_test")
    print()    
    remove_book_test("Remove books test 1:", remove_book(book_test1, "Harry Potter and the Sorcerers Stone", "Fiction"), book_test6)
    remove_book_test("Remove books test 2:", remove_book(book_test5, "Never Let Me Go", "Fiction"), book_test6)
    remove_book_test("Remove books test 3:", remove_book(book_test4, "The Silence of the Lambs", "Thrillers"), book_test6)

    #Fucntion 3 Test Calls
    print ("Function 3 Test Calls")
    print ("get_books_by_category_test")
    print()
    get_books_by_category_test(" get books for category test 1:", 7, get_books_by_category(book_dictionary, "Adventure"))
    get_books_by_category_test(" get books for category test 2:", 24, get_books_by_category(book_dictionary, "Business"))
    get_books_by_category_test(" get books for category test 3:", 7, get_books_by_category(book_dictionary, "Comics"))
    
    total_passed += passed
    
    print("\nTotal Tests:", test, "\nTests Passed:", passed, "\nTests Failed:", failed)
    print()
    
    #Set the testing variables to 0 to begin
    test = 0
    passed = 0
    failed = 0    
    

    
    #Fucntion 4 Test Calls
    print ("Function 4 Test Calls")
    print ("get_books_by_rate_test")
    get_books_by_rate_test(" get books for category test 1:", "9", get_books_by_rate(book_dictionary, 3))
    get_books_by_rate_test(" get books for category test 2:", "5", get_books_by_rate(book_dictionary, 5))
    get_books_by_rate_test(" get books for category test 3:", "69", get_books_by_rate(book_dictionary, 4))
    
    total_passed += passed
    
    print()
    print("\nTotal Tests:", test, "\nTests Passed:", passed, "\nTests Failed:", failed)
    
    #Set the testing variables to 0 to begin
    test = 0
    passed = 0
    failed = 0    
    
    #Function 5 Test Calls 
    
    print ("Function 5 Test Calls")
    print ("get_book_by_title")
    get_book_by_title_test("Categories for book title test 1:", True,get_book_by_title(book_dictionary, "Antiques Con"))
    get_book_by_title_test("Categories for book title test 2:", True,get_book_by_title(book_dictionary, "Bring Me Back"))
    get_book_by_title_test("Categories for book title test 3:", True,get_book_by_title(book_dictionary, "Homecoming (A Chloe Fine Psychological Suspense Mystery Book 5)"))
    
    total_passed += passed
    
    print("\nTotal Tests:", test, "\nTests Passed:", passed, "\nTests Failed:", failed)
    print()
    
    #Set the testing variables to 0 to begin
    test = 0
    passed = 0
    failed = 0    
    
    #Function 6 Test Calls
    print ("Function 6 Test Calls")
    print ("get_books_by_author_test")
    get_books_by_author_test(" get books for author test 1:", 3, get_books_by_author(book_dictionary, "Andrzej Sapkowski"))
    get_books_by_author_test(" get books for author test 2:", 2, get_books_by_author(book_dictionary, "Brandon Sanderson"))
    get_books_by_author_test(" get books for author test 3:", 4, get_books_by_author(book_dictionary, "Barbara Allan"))
    
    total_passed += passed
    
    print("\nTotal Tests:", test, "\nTests Passed:", passed, "\nTests Failed:", failed)
    print()

    #Set the testing variables to 0 to begin
    test = 0
    passed = 0
    failed = 0
    
    #Function 7 Test Calls
    print ("Function 7 Test Calls")
    print ("get_books_by_publisher_test")
    get_books_by_publisher_test(" get_books_by_publisher_test", 12, get_books_by_publisher(book_dictionary, "HarperCollins UK"))
    get_books_by_publisher_test(" get_books_by_publisher_test", 12, get_books_by_publisher(book_dictionary, "Hachette UK"))
    get_books_by_publisher_test(" get_books_by_publisher_test", 2, get_books_by_publisher(book_dictionary, "Kensington Publishing Corp."))
    
    total_passed += passed
    
    print("\nTotal Tests:", test, "\nTests Passed:", passed, "\nTests Failed:", failed)
    print()
    
    #Set the testing variables to 0 to begin
    test = 0
    passed = 0
    failed = 0    

    #Function 8 Test Calls
    print ("Function 8 Test Calls")
    print ("categories_for_book_title_test")
    categories_for_book_title_test("categories_for_book_title_test 1", 3,get_all_categories_for_book_title(book_dictionary, "Antiques Con"))
    categories_for_book_title_test("categories_for_book_title_test: 2", 3,get_all_categories_for_book_title(book_dictionary, "Bring Me Back"))
    categories_for_book_title_test("categories_for_book_title_test 3", 2,get_all_categories_for_book_title(book_dictionary, "Homecoming (A Chloe Fine Psychological Suspense Mystery Book 5)"))
    
    total_passed += passed
    
    print("\nTotal Tests:", test, "\nTests Passed:", passed, "\nTests Failed:", failed)
    print()
    
    print ("total Passed", total_passed)