#Zarif Khan 101224172
#Aiden Hepburn 101220580
#Chen Chen 101235800
#Ben Metcalfe 101234641
#March 12, 2022
#Version 1.0

def book_category_dictionary (file_one)->dict():
    """This function reads a csv file, and returns the places the books listed, in their respective categories
    
    >>>book_category_dictionary(google_books_dataset.csv)
    {'Fiction': [{'title': "Antiques Roadkill: A Trash 'n' Treasures Mystery", 'author': 'Barbara Allan', 'rating': '3.3', 'publisher': 'Kensington Publishing Corp.', 'pages': '288', 'language': 'English'},......] 
    
    """
    file = open(file_one)

#rating publisher pages category language

    book_dictionary = {}
    lst_one=[]

    for line in file:        
        line = line.strip("\n").split(",")
        if line[0]!="title" and line[2]!="N/A":


            lst_one = [] 
            saved_category = line.pop(5)
            dictionary1 = {"title": line[0], "author": line[1], "rating":line[2], "publisher": line[3], "pages": line [4], "language": line[5]}
            lst_one.append (dictionary1)
            
            if saved_category in book_dictionary:
                book_dictionary[saved_category] += (lst_one)
            else:
                book_dictionary.update({saved_category: lst_one})
                        
        elif line[0]!= "title":
            
            saved_category = line.pop(5)
            dictionary1 = {"title": line[0], "author": line[1], "rating":line[2], "publisher": line[3], "pages": line [4], "language": line[5]}
            lst_one.append (dictionary1)
            
            if saved_category in book_dictionary:
                book_dictionary[saved_category] += (lst_one)
            
            else:
                book_dictionary.update({saved_category: lst_one})
                
    file.close()
    for category in book_dictionary:
        category_books = book_dictionary.get(category)
        if len(category_books) > 1:
                occurences = {}
                for books in category_books:
                    title = books.get('title')
                    if occurences.get(title): occurences.update({title : occurences.get(title)+1})
                    else: occurences.update({title : 1})
                if occurences.get(title) > 1:
                    for books in category_books:
                            title = books.get('title')
                            if occurences.get(title) > 1:
                                for index in range(occurences.get(title)):
                                        if books in category_books:
                                            category_books.pop(category_books.index(books))   
                                            
    return book_dictionary

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#book_dictionary = book_category_dictionary(r"C:\Users\ben_m\Downloads\ECOR 1043\google_books_dataset.csv")


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
    
    title, author, language, publisher, category, rating, pages = book_info
    
    for key in dictionary:
        if key == category:
            dicc = {"title":title, "author":author, "language":language, "publisher":publisher, "rating":rating, "pages":pages}
            dictionary[key].append(dicc)
            print ("The book has been added correctly")
        elif key != category: 
            print ("There was an error adding the book")            
            
    return dictionary, "the book has been added correctly"


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


#Funtion 4 (Ben Metcalfe 101234641)
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


         
#Function 7 (Ben Metcalfe 101234641)

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
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Functions 1 - sort_books_title - Zarif Khan 101224172
def sort_books_title(dictionary : dict) -> list:
    """This fucntion will sort the books based on the titles in alphabetical order
    
    >>>sort_books_author(book_dictionary)
    
    
    [{'title': 'Business Strategy (The Brian Tracy Success Library)', 'author': 'Brian Tracy', 'language': None, 'rating': 'N/A', 'publisher': 'AMACOM', 'category': ['Economics', 'Business'], 'pages': '112'}, {'title': 'Management (The Brian Tracy Success Library)', 'author': 'Brian Tracy', 'language': None, 'rating': 'N/A', 'publisher': 'AMACOM', 'category': ['Economics', 'Biography', 'Management'], 'pages': '112'}, {'title': 'Marketing (The Brian Tracy Success Library)', 'author': 'Brian Tracy', 'language': None, 'rating': 'N/A', 'publisher': 'AMACOM', 'category': ['Economics'], 'pages': '112'}, {'title': 'Personal Success (The Brian Tracy Success Library)', 'author': 'Brian Tracy', 'language': None, 'rating': 'N/A', 'publisher': 'AMACOM', 'category': ['Economics', 'Business'], 'pages': '112'}, {'title': 'The Essentials of Finance and Accounting for Nonfinancial Managers', 'author': 'Edward Fields', 'language': None, 'rating': 'N/A', 'publisher': 'AMACOM', 'category': ['Economics', 'Money Management', 'Business'], 'pages': '320'}, {'title': 'Mrs. Pollifax Unveiled', 'author': 'Dorothy Gilman', 'language': None, 'rating': '3.9', 'publisher': 'Ballantine Books', 'category': ['Fiction', 'Detective'], 'pages': '208'}, {'title': 'Eat That Frog!: 21 Great Ways to Stop Procrastinating and Get More Done in Less Time. Edition 3', 'author': 'Brian Tracy', 'language': None, 'rating': '4.7', 'publisher': 'Berrett-Koehler Publishers', 'category': ['Economics', 'Business'], 'pages': '144'}, {'title': 'Goals!: How to Get Everything You Want -- Faster Than You Ever Thought Possible. Edition 2', 'author': 'Brian Tracy', 'language': None, 'rating': '4.3', 'publisher': 'Berrett-Koehler Publishers', 'category': ['Economics'], 'pages': '288'}, {'title': 'A Trace of Crime (a Keri Locke Mystery Book #4)', 'author': 'Blake Pierce', 'language': None, 'rating': '4.7', 'publisher': 'Blake Pierce', 'category': ['Fiction', 'Detective', 'Mystery'], 'pages': '250'}, {'title': 'A Trace of Vice (a Keri Locke Mystery Book #3)', 'author': 'Blake Pierce', 'language': None, 'rating': '4.8', 'publisher': 'Blake Pierce', 'category': ['Fiction'], 'pages': '250'}, {'title': 'Homecoming (A Chloe Fine Psychological Suspense Mystery Book 5)', 'author': 'Blake Pierce', 'language': None, 'rating': '4.6', 'publisher': 'Blake Pierce', 'category': ['Detective', 'Mystery'], 'pages': '250'}, {'title': 'Once Missed (A Riley Paige Mystery Book 16)', 'author': 'Blake Pierce', 'language': None, 'rating': '4.4', 'publisher': 'Blake Pierce', 'category': ['Thrillers', 'Detective', 'Mystery'], 'pages': '250'}, {'title': 'Riley Paige Mystery Bundle: Once Gone (#1) and Once Taken (#2)', 'author': 'Blake Pierce', 'language': None, 'rating': '4.5', 'publisher': 'Blake Pierce', 'category': ['Economics', 'Thrillers', 'Detective', 'Mystery'], 'pages': '250'}, {'title': 'Watching (The Making of Riley Paige Book 1)', 'author': 'Blake Pierce', 'language': None, 'rating': '4.6', 'publisher': 'Blake Pierce', 'category': ['Management', 'Detective', 'Mystery'], 'pages': '250'}, {'title': 'Becoming Steve Jobs: The Evolution of a Reckless Upstart into a Visionary Leader', 'author': 'Brent Schlender', 'language': None, 'rating': '4.6', 'publisher': 'Crown Business', 'category': ['Biography', 'Information Technology', 'Business'], 'pages': '464'}, {'title': 'Rework', 'author': 'Jason Fried', 'language': None, 'rating': '4.1', 'publisher': 'Currency', 'category': ['Economics', 'Business'], 'pages': '288'}, {'title': 'The Joker', 'author': 'Brian Azzarello', 'language': None, 'rating': '4.4', 'publisher': 'DC', 'category': ['Comics'], 'pages': '130'}, {'title': 'Young Justice Vol. 1', 'author': 'Art Baltazar', 'language': None, 'rating': '4.1', 'publisher': 'DC', 'category': ['Comics', 'Superheroes'], 'pages': '164'}, {'title': 'Watchmen (2019 Edition)', 'author': 'Alan Moore', 'language': None, 'rating': '4.2', 'publisher': 'DC Comics', 'category': ['Comics', 'Business', 'Superheroes'], 'pages': '448'}, {'title': "'Salem's Lot", 'author': 'Stephen King', 'language': None, 'rating': '4.4', 'publisher': 'Hachette UK', 'category': ['Thrillers', 'Fiction'], 'pages': '300'}, {'title': 'No Mercy: The brand new novel from the Queen of Crime', 'author': 'Martina Cole', 'language': None, 'rating': 'N/A', 'publisher': 'Hachette UK', 'category': ['Thrillers', 'Fiction'], 'pages': '416'}, {'title': 'Shantaram', 'author': 'Gregory David Roberts', 'language': None, 'rating': '4.5', 'publisher': 'Hachette UK', 'category': ['Thrillers', 'Fiction', 'Detective'], 'pages': '944'}, {'title': 'Sword of Destiny: Witcher 2: Tales of the Witcher', 'author': 'Andrzej Sapkowski', 'language': None, 'rating': '4.8', 'publisher': 'Hachette UK', 'category': ['Adventure', 'Mythical Creatures', 'Fiction'], 'pages': '400'}, {'title': 'Tall Tales and Wee Stories: The Best of Billy Connolly', 'author': 'Billy Connolly', 'language': None, 'rating': '5', 'publisher': 'Hachette UK', 'category': ['Economics', 'Biography', 'Humor'], 'pages': '336'}, {'title': 'The Black Box', 'author': 'Michael Connelly', 'language': None, 'rating': '4', 'publisher': 'Hachette UK', 'category': ['Thrillers', 'Fiction', 'Crime', 'Mystery'], 'pages': '448'}, {'title': 'The Guardians: The explosive new thriller from international bestseller John Grisham', 'author': 'John Grisham', 'language': None, 'rating': 'N/A', 'publisher': 'Hachette UK', 'category': ['Economics', 'Thrillers', 'Fiction', 'Legal'], 'pages': '384'}, {'title': 'The Malady and Other Stories: An Andrzej Sapkowski Sampler', 'author': 'Andrzej Sapkowski', 'language': None, 'rating': '4.8', 'publisher': 'Hachette UK', 'category': ['Adventure', 'Fiction', 'Fantasy'], 'pages': '96'}, {'title': 'The Name of the Wind: The Kingkiller Chronicle:Book 1', 'author': 'Patrick Rothfuss', 'language': None, 'rating': '4.3', 'publisher': 'Hachette UK', 'category': ['Fiction', 'Fantasy'], 'pages': '672'}, {'title': 'The Secrets of Saving and Investing with Alvin Hall: Simple Strategies to Make Your Money Go Further', 'author': 'Alvin Hall', 'language': None, 'rating': '3.7', 'publisher': 'Hachette UK', 'category': ['Finance', 'Business', 'Economics', 'Money Management', 'Thrillers', 'Investing'], 'pages': '30'}, {'title': 'The Tower of the Swallow: Witcher 6', 'author': 'Andrzej Sapkowski', 'language': None, 'rating': '4.6', 'publisher': 'Hachette UK', 'category': ['Epic', 'Fiction', 'Fantasy'], 'pages': '400'}, {'title': 'The Way Of Shadows: Book 1 of the Night Angel', 'author': 'Brent Weeks', 'language': None, 'rating': '4.7', 'publisher': 'Hachette UK', 'category': ['Adventure', 'Epic', 'Fantasy'], 'pages': '688'}, {'title': 'Freakonomics Rev Ed: A Rogue Economist Explores the Hidden Side of Everything', 'author': 'Steven D. Levitt', 'language': None, 'rating': '3.8', 'publisher': 'Harper Collins', 'category': ['Economics', 'Social Science', 'Business'], 'pages': '336'}, {'title': 'Little Girl Lost: A Lucy Black Thriller', 'author': 'Brian McGilloway', 'language': None, 'rating': '4', 'publisher': 'Harper Collins', 'category': ['Economics', 'Thrillers', 'Fiction', 'Mystery'], 'pages': '336'}, {'title': 'Secrets of the Millionaire Mind: Mastering the Inner Game of Wealth', 'author': 'T. Harv Eker', 'language': None, 'rating': '4.6', 'publisher': 'Harper Collins', 'category': ['Economics', 'Business'], 'pages': '224'}, {'title': 'Think Like a Freak: The Authors of Freakonomics Offer to Retrain Your Brain', 'author': 'Steven D. Levitt', 'language': None, 'rating': '4.3', 'publisher': 'Harper Collins', 'category': ['Business'], 'pages': '304'}, {'title': 'Platform: Get Noticed in a Noisy World', 'author': 'Michael Hyatt', 'language': None, 'rating': '4.6', 'publisher': 'HarperCollins Leadership', 'category': ['Economics', 'Business'], 'pages': '288'}, {'title': 'Selling 101: What Every Successful Sales Professional Needs to Know', 'author': 'Zig Ziglar', 'language': None, 'rating': '3.8', 'publisher': 'HarperCollins Leadership', 'category': ['Business'], 'pages': '112'}, {'title': 'A Feast for Crows (A Song of Ice and Fire. Book 4)', 'author': 'George R.R. Martin', 'language': None, 'rating': '4.5', 'publisher': 'HarperCollins UK', 'category': ['Adventure', 'Epic', 'Fiction', 'Fantasy'], 'pages': '864'}, {'title': 'A Game of Thrones: The Story Continues Books 1-5: A Game of Thrones. A Clash of Kings. A Storm of Swords. A Feast for Crows. A Dance with Dragons (A Song of Ice and Fire)', 'author': 'George R.R. Martin', 'language': None, 'rating': '4.5', 'publisher': 'HarperCollins UK', 'category': ['Epic', 'Economics', 'Fiction', 'Adventure', 'Fantasy'], 'pages': '4544'}, {'title': 'After Anna', 'author': 'Alex Lake', 'language': None, 'rating': '4.1', 'publisher': 'HarperCollins UK', 'category': ['Adventure', 'Thrillers', 'Fiction', 'Mystery'], 'pages': '416'}, {'title': 'And Then There Were None', 'author': 'Agatha Christie', 'language': None, 'rating': '4.6', 'publisher': 'HarperCollins UK', 'category': ['Thrillers', 'Fiction', 'Detective', 'Mystery'], 'pages': '224'}, {'title': 'Bring Me Back', 'author': 'B A Paris', 'language': None, 'rating': '3.8', 'publisher': 'HarperCollins UK', 'category': ['Thrillers', 'Fiction', 'Crime'], 'pages': '368'}, {'title': 'Predictably Irrational: The Hidden Forces that Shape Our Decisions', 'author': 'Dan Ariely', 'language': None, 'rating': '4', 'publisher': 'HarperCollins UK', 'category': ['Economics', 'Psychology', 'Business'], 'pages': '304'}, {'title': 'Prince of Thorns (The Broken Empire. Book 1)', 'author': 'Mark Lawrence', 'language': None, 'rating': '4.2', 'publisher': 'HarperCollins UK', 'category': ['Fiction', 'Fantasy'], 'pages': '416'}, {'title': 'The Lord of the Rings: The Fellowship of the Ring. The Two Towers. The Return of the King', 'author': 'J. R. R. Tolkien', 'language': None, 'rating': '4.6', 'publisher': 'HarperCollins UK', 'category': ['Fiction', 'Fantasy'], 'pages': '1216'}, {'title': 'The Mysterious Affair at Styles', 'author': 'Agatha Christie', 'language': None, 'rating': '4.4', 'publisher': 'HarperCollins UK', 'category': ['Horror', 'Fiction', 'Classics', 'Thrillers', 'Detective'], 'pages': '208'}, {'title': 'The Painted Man (The Demon Cycle. Book 1)', 'author': 'Peter V. Brett', 'language': None, 'rating': '4.5', 'publisher': 'HarperCollins UK', 'category': ['Thrillers', 'Fiction', 'Fantasy', 'Business'], 'pages': '544'}, {'title': 'The Red Signal: An Agatha Christie Short Story', 'author': 'Agatha Christie', 'language': None, 'rating': '5', 'publisher': 'HarperCollins UK', 'category': ['Traditional', 'Fiction', 'Detective', 'Mystery'], 'pages': '40'}, {'title': 'The Vagrant (The Vagrant Trilogy)', 'author': 'Peter Newman', 'language': None, 'rating': '4.2', 'publisher': 'HarperCollins UK', 'category': ['Fiction', 'Fantasy'], 'pages': '416'}, {'title': 'Antiques Chop', 'author': 'Barbara Allan', 'language': None, 'rating': '4.5', 'publisher': 'Kensington Books', 'category': ['Fiction', 'Detective', 'Mystery'], 'pages': '240'}, {'title': 'Antiques Con', 'author': 'Barbara Allan', 'language': None, 'rating': '4.8', 'publisher': 'Kensington Books', 'category': ['Fiction', 'Detective', 'Mystery'], 'pages': '288'}, {'title': 'Killer Blonde', 'author': 'Laura Levine', 'language': None, 'rating': '4', 'publisher': 'Kensington Books', 'category': ['Fiction', 'Detective'], 'pages': '288'}, {'title': 'Antiques Knock-Off', 'author': 'Barbara Allan', 'language': None, 'rating': '4.3', 'publisher': 'Kensington Publishing Corp.', 'category': ['Fiction', 'Detective', 'Mystery'], 'pages': '240'}, {'title': "Antiques Roadkill: A Trash 'n' Treasures Mystery", 'author': 'Barbara Allan', 'language': None, 'rating': '3.3', 'publisher': 'Kensington Publishing Corp.', 'category': ['Fiction', 'Detective', 'Mystery'], 'pages': '288'}, {'title': 'How to Understand Business Finance: Edition 2', 'author': 'Bob Cinnamon', 'language': None, 'rating': '3.5', 'publisher': 'Kogan Page Publishers', 'category': ['Economics', 'Business'], 'pages': '176'}, {'title': "Chronicle of the Unhewn Throne: (The Emperor's Blades. The Providence of Fire. The Last Mortal Bond)", 'author': 'Brian Staveley', 'language': None, 'rating': '4.3', 'publisher': 'Macmillan', 'category': ['Fiction', 'Fantasy'], 'pages': '1728'}, {'title': 'Deadpool Kills the Marvel Universe', 'author': 'Cullen Bunn', 'language': None, 'rating': '4.2', 'publisher': 'Marvel Entertainment', 'category': ['Comics'], 'pages': '96'}, {'title': 'Immortal Hulk Vol. 1: Or Is He Both?', 'author': 'Al Ewing', 'language': None, 'rating': '4.4', 'publisher': 'Marvel Entertainment', 'category': ['Comics', 'Superheroes'], 'pages': '128'}, {'title': 'Spider-Man: Anti-Venom', 'author': 'Dan Slott', 'language': None, 'rating': '4', 'publisher': 'Marvel Entertainment', 'category': ['Superheroes'], 'pages': '96'}, {'title': 'Spider-Verse: Volume 1', 'author': 'Dan Slott', 'language': None, 'rating': '4.4', 'publisher': 'Marvel Entertainment', 'category': ['Superheroes'], 'pages': '624'}, {'title': 'Ultimate Spider-Man Vol. 11: Carnage', 'author': 'Brian Michael Bendis', 'language': None, 'rating': '4.1', 'publisher': 'Marvel Entertainment', 'category': ['Comics'], 'pages': '144'}, {'title': 'Venomized', 'author': 'Cullen Bunn', 'language': None, 'rating': '4.5', 'publisher': 'Marvel Entertainment', 'category': ['Comics'], 'pages': '136'}, {'title': 'Permanent Record', 'author': 'Edward Snowden', 'language': None, 'rating': '4.6', 'publisher': 'Metropolitan Books', 'category': ['Legal', 'Biography'], 'pages': '352'}, {'title': 'In Dark Company: A Kate Burkholder Short Story', 'author': 'Linda Castillo', 'language': None, 'rating': '4.3', 'publisher': 'Minotaur Books', 'category': ['Thrillers', 'Fiction'], 'pages': '60'}, {'title': 'Night of the Bold (Kings and Sorcerers Book 6)', 'author': 'Morgan Rice', 'language': None, 'rating': '4.3', 'publisher': 'Morgan Rice', 'category': ['Fiction', 'Fantasy'], 'pages': '250'}, {'title': 'The Weight of Honor (Kings and Sorcerers Book 3)', 'author': 'Morgan Rice', 'language': None, 'rating': '4.4', 'publisher': 'Morgan Rice', 'category': ['Fiction', 'Fantasy'], 'pages': '250'}, {'title': 'Summary: Think and Grow Rich', 'author': 'Nine99 Innovation Lab', 'language': None, 'rating': 'N/A', 'publisher': 'Nine99 Innovation Lab (OPC) Pvt Ltd', 'category': ['Economics', 'Business'], 'pages': '14'}, {'title': 'We', 'author': 'Yevgeny Zamyatin', 'language': None, 'rating': '4.3', 'publisher': 'Pan', 'category': ['Fiction', 'Fantasy'], 'pages': '226'}, {'title': 'Total Control', 'author': 'David Baldacci', 'language': None, 'rating': '4', 'publisher': 'Pan Macmillan', 'category': ['Thrillers', 'Fiction', 'Crime', 'Mystery'], 'pages': '624'}, {'title': 'Twas The Nightshift Before Christmas: Festive hospital diaries from the author of million-copy hit This is Going to Hurt', 'author': 'Adam Kay', 'language': None, 'rating': '4.7', 'publisher': 'Pan Macmillan', 'category': ['Humor'], 'pages': '112'}, {'title': 'Boy Erased: A Memoir', 'author': 'Garrard Conley', 'language': None, 'rating': '4', 'publisher': 'Penguin', 'category': ['Economics', 'Biography'], 'pages': '352'}, {'title': 'Getting Things Done: The Art of Stress-Free Productivity', 'author': 'David Allen', 'language': None, 'rating': '4.5', 'publisher': 'Penguin', 'category': ['Economics'], 'pages': '352'}, {'title': 'No One Is Too Small to Make a Difference', 'author': 'Greta Thunberg', 'language': None, 'rating': '5', 'publisher': 'Penguin', 'category': ['Biography'], 'pages': '112'}, {'title': 'The Infinite Game', 'author': 'Simon Sinek', 'language': None, 'rating': '3.8', 'publisher': 'Penguin', 'category': ['Business'], 'pages': '272'}, {'title': 'The Magic of Thinking Big', 'author': 'David J. Schwartz', 'language': None, 'rating': '4.6', 'publisher': 'Penguin', 'category': ['Economics', 'Business'], 'pages': '256'}, {'title': "Final Option: 'The best one yet'", 'author': 'Clive Cussler', 'language': None, 'rating': '5', 'publisher': 'Penguin UK', 'category': ['Thrillers', 'Fiction', 'Crime', 'Mystery'], 'pages': '400'}, {'title': 'Happy: Why More or Less Everything is Absolutely Fine', 'author': 'Derren Brown', 'language': None, 'rating': '4', 'publisher': 'Random House', 'category': ['Social Science'], 'pages': '576'}, {'title': 'The Power of Habit: Why We Do What We Do in Life and Business', 'author': 'Charles Duhigg', 'language': None, 'rating': '4.1', 'publisher': 'Random House', 'category': ['Economics'], 'pages': '416'}, {'title': 'Financial Statements. Revised and Expanded Edition: A Step-by-Step Guide to Understanding and Creating Financial Reports', 'author': 'Thomas Ittelson', 'language': None, 'rating': '4', 'publisher': 'Red Wheel/Weiser', 'category': ['Economics'], 'pages': '288'}, {'title': 'How To Win Friends and Influence People', 'author': 'Dale Carnegie', 'language': None, 'rating': '4.3', 'publisher': 'Simon and Schuster', 'category': ['Economics', 'Psychology'], 'pages': '320'}, {'title': 'Principles: Life and Work', 'author': 'Ray Dalio', 'language': None, 'rating': '4.7', 'publisher': 'Simon and Schuster', 'category': ['Economics', 'Business'], 'pages': '592'}, {'title': 'Start Day Trading Now: A Quick and Easy Introduction to Making Money While Managing Your Risk', 'author': 'Michael Sincere', 'language': None, 'rating': '5', 'publisher': 'Simon and Schuster', 'category': ['Economics', 'Business'], 'pages': '224'}, {'title': 'The Memoirs of Sherlock Holmes', 'author': 'Arthur Conan Doyle', 'language': None, 'rating': '4.2', 'publisher': 'Simon and Schuster', 'category': ['Fiction', 'Classics', 'Mystery', 'Thrillers', 'Detective'], 'pages': '320'}, {'title': 'Edgedancer: From the Stormlight Archive', 'author': 'Brandon Sanderson', 'language': None, 'rating': '4.8', 'publisher': 'Tor Books', 'category': ['Adventure', 'Fiction'], 'pages': '226'}, {'title': 'Mistborn Trilogy: The Final Empire. The Well of Ascension. The Hero of Ages', 'author': 'Brandon Sanderson', 'language': None, 'rating': '4.7', 'publisher': 'Tor Books', 'category': ['Fantasy'], 'pages': '1712'}, {'title': 'We Should All Be Feminists', 'author': 'Chimamanda Ngozi Adichie', 'language': None, 'rating': '4.2', 'publisher': 'Vintage', 'category': ['Social Science'], 'pages': '32'}, {'title': "The Girl in the Spider's Web: A Lisbeth Salander novel: continuing Stieg Larsson's Millennium Series", 'author': 'David Lagercrantz', 'language': None, 'rating': '4.1', 'publisher': 'Vintage Crime/Black Lizard', 'category': ['Thrillers', 'Fiction', 'Mystery'], 'pages': '416'}, {'title': 'Platform Revolution: How Networked Markets Are Transforming the Economy and How to Make Them Work for You', 'author': 'Geoffrey G. Parker', 'language': None, 'rating': '4.5', 'publisher': 'W. W. Norton & Company', 'category': ['Business'], 'pages': '256'}]
    """


    
    lst = []
    
    for category in dictionary:
        for books in dictionary[category]:
            
            #Searching for duplicate titles
            same_title = False
            for book_info in lst:
                if book_info.get('title') == books.get('title'): 
                    same_title = True

            if not same_title:
                category = set()
                for matching_category in dictionary:
                    for matching_book in dictionary.get(matching_category):
                            if matching_book.get('title') == books.get('title'): 
                                category.add(matching_category) 
                                
                                
                #now formatted properly                      
                lst.append({
                    "title" : books.get('title'),
                    "author" : books.get('author'),
                    "language" : books.get('language '),
                    "rating" : books.get('rating'),
                    "publisher" : books.get('publisher'),
                    "category" : list(category),
                    "pages" : books.get('pages'),
                })       
                
    # Bubble Sort Algorithm 
    
    for i in range(len(lst)):
            for j in range(len(lst) - 1 - i):
                a = lst[j]
                b = lst[j + 1]
                        
                if a["publisher"] > b["publisher"]:
                    lst[j], lst[j+1] = lst[j + 1], lst[j]
                if a["publisher"] == b["publisher"]:
                    if a["title"] > b["title"]:
                        lst[j], lst[j+1] = lst[j + 1], lst[j]
        
    return lst


#Function 2 - sort_books_publisher - Aiden Hepburn 101220580
def sort_books_publisher(dictionary : dict) -> list:
    """This fucntion will sort the books based on the titles in alphabetical order
    
    >>>sort_books_author(book_dictionary)
    
    
    [{'title': 'Business Strategy (The Brian Tracy Success Library)', 'author': 'Brian Tracy', 'language': None, 'rating': 'N/A', 'publisher': 'AMACOM', 'category': ['Economics', 'Business'], 'pages': '112'}, {'title': 'Management (The Brian Tracy Success Library)', 'author': 'Brian Tracy', 'language': None, 'rating': 'N/A', 'publisher': 'AMACOM', 'category': ['Economics', 'Biography', 'Management'], 'pages': '112'}, {'title': 'Marketing (The Brian Tracy Success Library)', 'author': 'Brian Tracy', 'language': None, 'rating': 'N/A', 'publisher': 'AMACOM', 'category': ['Economics'], 'pages': '112'}, {'title': 'Personal Success (The Brian Tracy Success Library)', 'author': 'Brian Tracy', 'language': None, 'rating': 'N/A', 'publisher': 'AMACOM', 'category': ['Economics', 'Business'], 'pages': '112'}, {'title': 'The Essentials of Finance and Accounting for Nonfinancial Managers', 'author': 'Edward Fields', 'language': None, 'rating': 'N/A', 'publisher': 'AMACOM', 'category': ['Economics', 'Money Management', 'Business'], 'pages': '320'}, {'title': 'Mrs. Pollifax Unveiled', 'author': 'Dorothy Gilman', 'language': None, 'rating': '3.9', 'publisher': 'Ballantine Books', 'category': ['Fiction', 'Detective'], 'pages': '208'}, {'title': 'Eat That Frog!: 21 Great Ways to Stop Procrastinating and Get More Done in Less Time. Edition 3', 'author': 'Brian Tracy', 'language': None, 'rating': '4.7', 'publisher': 'Berrett-Koehler Publishers', 'category': ['Economics', 'Business'], 'pages': '144'}, {'title': 'Goals!: How to Get Everything You Want -- Faster Than You Ever Thought Possible. Edition 2', 'author': 'Brian Tracy', 'language': None, 'rating': '4.3', 'publisher': 'Berrett-Koehler Publishers', 'category': ['Economics'], 'pages': '288'}, {'title': 'A Trace of Crime (a Keri Locke Mystery Book #4)', 'author': 'Blake Pierce', 'language': None, 'rating': '4.7', 'publisher': 'Blake Pierce', 'category': ['Fiction', 'Detective', 'Mystery'], 'pages': '250'}, {'title': 'A Trace of Vice (a Keri Locke Mystery Book #3)', 'author': 'Blake Pierce', 'language': None, 'rating': '4.8', 'publisher': 'Blake Pierce', 'category': ['Fiction'], 'pages': '250'}, {'title': 'Homecoming (A Chloe Fine Psychological Suspense Mystery Book 5)', 'author': 'Blake Pierce', 'language': None, 'rating': '4.6', 'publisher': 'Blake Pierce', 'category': ['Detective', 'Mystery'], 'pages': '250'}, {'title': 'Once Missed (A Riley Paige Mystery Book 16)', 'author': 'Blake Pierce', 'language': None, 'rating': '4.4', 'publisher': 'Blake Pierce', 'category': ['Thrillers', 'Detective', 'Mystery'], 'pages': '250'}, {'title': 'Riley Paige Mystery Bundle: Once Gone (#1) and Once Taken (#2)', 'author': 'Blake Pierce', 'language': None, 'rating': '4.5', 'publisher': 'Blake Pierce', 'category': ['Economics', 'Thrillers', 'Detective', 'Mystery'], 'pages': '250'}, {'title': 'Watching (The Making of Riley Paige Book 1)', 'author': 'Blake Pierce', 'language': None, 'rating': '4.6', 'publisher': 'Blake Pierce', 'category': ['Management', 'Detective', 'Mystery'], 'pages': '250'}, {'title': 'Becoming Steve Jobs: The Evolution of a Reckless Upstart into a Visionary Leader', 'author': 'Brent Schlender', 'language': None, 'rating': '4.6', 'publisher': 'Crown Business', 'category': ['Biography', 'Information Technology', 'Business'], 'pages': '464'}, {'title': 'Rework', 'author': 'Jason Fried', 'language': None, 'rating': '4.1', 'publisher': 'Currency', 'category': ['Economics', 'Business'], 'pages': '288'}, {'title': 'The Joker', 'author': 'Brian Azzarello', 'language': None, 'rating': '4.4', 'publisher': 'DC', 'category': ['Comics'], 'pages': '130'}, {'title': 'Young Justice Vol. 1', 'author': 'Art Baltazar', 'language': None, 'rating': '4.1', 'publisher': 'DC', 'category': ['Comics', 'Superheroes'], 'pages': '164'}, {'title': 'Watchmen (2019 Edition)', 'author': 'Alan Moore', 'language': None, 'rating': '4.2', 'publisher': 'DC Comics', 'category': ['Comics', 'Business', 'Superheroes'], 'pages': '448'}, {'title': "'Salem's Lot", 'author': 'Stephen King', 'language': None, 'rating': '4.4', 'publisher': 'Hachette UK', 'category': ['Thrillers', 'Fiction'], 'pages': '300'}, {'title': 'No Mercy: The brand new novel from the Queen of Crime', 'author': 'Martina Cole', 'language': None, 'rating': 'N/A', 'publisher': 'Hachette UK', 'category': ['Thrillers', 'Fiction'], 'pages': '416'}, {'title': 'Shantaram', 'author': 'Gregory David Roberts', 'language': None, 'rating': '4.5', 'publisher': 'Hachette UK', 'category': ['Thrillers', 'Fiction', 'Detective'], 'pages': '944'}, {'title': 'Sword of Destiny: Witcher 2: Tales of the Witcher', 'author': 'Andrzej Sapkowski', 'language': None, 'rating': '4.8', 'publisher': 'Hachette UK', 'category': ['Adventure', 'Mythical Creatures', 'Fiction'], 'pages': '400'}, {'title': 'Tall Tales and Wee Stories: The Best of Billy Connolly', 'author': 'Billy Connolly', 'language': None, 'rating': '5', 'publisher': 'Hachette UK', 'category': ['Economics', 'Biography', 'Humor'], 'pages': '336'}, {'title': 'The Black Box', 'author': 'Michael Connelly', 'language': None, 'rating': '4', 'publisher': 'Hachette UK', 'category': ['Thrillers', 'Fiction', 'Crime', 'Mystery'], 'pages': '448'}, {'title': 'The Guardians: The explosive new thriller from international bestseller John Grisham', 'author': 'John Grisham', 'language': None, 'rating': 'N/A', 'publisher': 'Hachette UK', 'category': ['Economics', 'Thrillers', 'Fiction', 'Legal'], 'pages': '384'}, {'title': 'The Malady and Other Stories: An Andrzej Sapkowski Sampler', 'author': 'Andrzej Sapkowski', 'language': None, 'rating': '4.8', 'publisher': 'Hachette UK', 'category': ['Adventure', 'Fiction', 'Fantasy'], 'pages': '96'}, {'title': 'The Name of the Wind: The Kingkiller Chronicle:Book 1', 'author': 'Patrick Rothfuss', 'language': None, 'rating': '4.3', 'publisher': 'Hachette UK', 'category': ['Fiction', 'Fantasy'], 'pages': '672'}, {'title': 'The Secrets of Saving and Investing with Alvin Hall: Simple Strategies to Make Your Money Go Further', 'author': 'Alvin Hall', 'language': None, 'rating': '3.7', 'publisher': 'Hachette UK', 'category': ['Finance', 'Business', 'Economics', 'Money Management', 'Thrillers', 'Investing'], 'pages': '30'}, {'title': 'The Tower of the Swallow: Witcher 6', 'author': 'Andrzej Sapkowski', 'language': None, 'rating': '4.6', 'publisher': 'Hachette UK', 'category': ['Epic', 'Fiction', 'Fantasy'], 'pages': '400'}, {'title': 'The Way Of Shadows: Book 1 of the Night Angel', 'author': 'Brent Weeks', 'language': None, 'rating': '4.7', 'publisher': 'Hachette UK', 'category': ['Adventure', 'Epic', 'Fantasy'], 'pages': '688'}, {'title': 'Freakonomics Rev Ed: A Rogue Economist Explores the Hidden Side of Everything', 'author': 'Steven D. Levitt', 'language': None, 'rating': '3.8', 'publisher': 'Harper Collins', 'category': ['Economics', 'Social Science', 'Business'], 'pages': '336'}, {'title': 'Little Girl Lost: A Lucy Black Thriller', 'author': 'Brian McGilloway', 'language': None, 'rating': '4', 'publisher': 'Harper Collins', 'category': ['Economics', 'Thrillers', 'Fiction', 'Mystery'], 'pages': '336'}, {'title': 'Secrets of the Millionaire Mind: Mastering the Inner Game of Wealth', 'author': 'T. Harv Eker', 'language': None, 'rating': '4.6', 'publisher': 'Harper Collins', 'category': ['Economics', 'Business'], 'pages': '224'}, {'title': 'Think Like a Freak: The Authors of Freakonomics Offer to Retrain Your Brain', 'author': 'Steven D. Levitt', 'language': None, 'rating': '4.3', 'publisher': 'Harper Collins', 'category': ['Business'], 'pages': '304'}, {'title': 'Platform: Get Noticed in a Noisy World', 'author': 'Michael Hyatt', 'language': None, 'rating': '4.6', 'publisher': 'HarperCollins Leadership', 'category': ['Economics', 'Business'], 'pages': '288'}, {'title': 'Selling 101: What Every Successful Sales Professional Needs to Know', 'author': 'Zig Ziglar', 'language': None, 'rating': '3.8', 'publisher': 'HarperCollins Leadership', 'category': ['Business'], 'pages': '112'}, {'title': 'A Feast for Crows (A Song of Ice and Fire. Book 4)', 'author': 'George R.R. Martin', 'language': None, 'rating': '4.5', 'publisher': 'HarperCollins UK', 'category': ['Adventure', 'Epic', 'Fiction', 'Fantasy'], 'pages': '864'}, {'title': 'A Game of Thrones: The Story Continues Books 1-5: A Game of Thrones. A Clash of Kings. A Storm of Swords. A Feast for Crows. A Dance with Dragons (A Song of Ice and Fire)', 'author': 'George R.R. Martin', 'language': None, 'rating': '4.5', 'publisher': 'HarperCollins UK', 'category': ['Epic', 'Economics', 'Fiction', 'Adventure', 'Fantasy'], 'pages': '4544'}, {'title': 'After Anna', 'author': 'Alex Lake', 'language': None, 'rating': '4.1', 'publisher': 'HarperCollins UK', 'category': ['Adventure', 'Thrillers', 'Fiction', 'Mystery'], 'pages': '416'}, {'title': 'And Then There Were None', 'author': 'Agatha Christie', 'language': None, 'rating': '4.6', 'publisher': 'HarperCollins UK', 'category': ['Thrillers', 'Fiction', 'Detective', 'Mystery'], 'pages': '224'}, {'title': 'Bring Me Back', 'author': 'B A Paris', 'language': None, 'rating': '3.8', 'publisher': 'HarperCollins UK', 'category': ['Thrillers', 'Fiction', 'Crime'], 'pages': '368'}, {'title': 'Predictably Irrational: The Hidden Forces that Shape Our Decisions', 'author': 'Dan Ariely', 'language': None, 'rating': '4', 'publisher': 'HarperCollins UK', 'category': ['Economics', 'Psychology', 'Business'], 'pages': '304'}, {'title': 'Prince of Thorns (The Broken Empire. Book 1)', 'author': 'Mark Lawrence', 'language': None, 'rating': '4.2', 'publisher': 'HarperCollins UK', 'category': ['Fiction', 'Fantasy'], 'pages': '416'}, {'title': 'The Lord of the Rings: The Fellowship of the Ring. The Two Towers. The Return of the King', 'author': 'J. R. R. Tolkien', 'language': None, 'rating': '4.6', 'publisher': 'HarperCollins UK', 'category': ['Fiction', 'Fantasy'], 'pages': '1216'}, {'title': 'The Mysterious Affair at Styles', 'author': 'Agatha Christie', 'language': None, 'rating': '4.4', 'publisher': 'HarperCollins UK', 'category': ['Horror', 'Fiction', 'Classics', 'Thrillers', 'Detective'], 'pages': '208'}, {'title': 'The Painted Man (The Demon Cycle. Book 1)', 'author': 'Peter V. Brett', 'language': None, 'rating': '4.5', 'publisher': 'HarperCollins UK', 'category': ['Thrillers', 'Fiction', 'Fantasy', 'Business'], 'pages': '544'}, {'title': 'The Red Signal: An Agatha Christie Short Story', 'author': 'Agatha Christie', 'language': None, 'rating': '5', 'publisher': 'HarperCollins UK', 'category': ['Traditional', 'Fiction', 'Detective', 'Mystery'], 'pages': '40'}, {'title': 'The Vagrant (The Vagrant Trilogy)', 'author': 'Peter Newman', 'language': None, 'rating': '4.2', 'publisher': 'HarperCollins UK', 'category': ['Fiction', 'Fantasy'], 'pages': '416'}, {'title': 'Antiques Chop', 'author': 'Barbara Allan', 'language': None, 'rating': '4.5', 'publisher': 'Kensington Books', 'category': ['Fiction', 'Detective', 'Mystery'], 'pages': '240'}, {'title': 'Antiques Con', 'author': 'Barbara Allan', 'language': None, 'rating': '4.8', 'publisher': 'Kensington Books', 'category': ['Fiction', 'Detective', 'Mystery'], 'pages': '288'}, {'title': 'Killer Blonde', 'author': 'Laura Levine', 'language': None, 'rating': '4', 'publisher': 'Kensington Books', 'category': ['Fiction', 'Detective'], 'pages': '288'}, {'title': 'Antiques Knock-Off', 'author': 'Barbara Allan', 'language': None, 'rating': '4.3', 'publisher': 'Kensington Publishing Corp.', 'category': ['Fiction', 'Detective', 'Mystery'], 'pages': '240'}, {'title': "Antiques Roadkill: A Trash 'n' Treasures Mystery", 'author': 'Barbara Allan', 'language': None, 'rating': '3.3', 'publisher': 'Kensington Publishing Corp.', 'category': ['Fiction', 'Detective', 'Mystery'], 'pages': '288'}, {'title': 'How to Understand Business Finance: Edition 2', 'author': 'Bob Cinnamon', 'language': None, 'rating': '3.5', 'publisher': 'Kogan Page Publishers', 'category': ['Economics', 'Business'], 'pages': '176'}, {'title': "Chronicle of the Unhewn Throne: (The Emperor's Blades. The Providence of Fire. The Last Mortal Bond)", 'author': 'Brian Staveley', 'language': None, 'rating': '4.3', 'publisher': 'Macmillan', 'category': ['Fiction', 'Fantasy'], 'pages': '1728'}, {'title': 'Deadpool Kills the Marvel Universe', 'author': 'Cullen Bunn', 'language': None, 'rating': '4.2', 'publisher': 'Marvel Entertainment', 'category': ['Comics'], 'pages': '96'}, {'title': 'Immortal Hulk Vol. 1: Or Is He Both?', 'author': 'Al Ewing', 'language': None, 'rating': '4.4', 'publisher': 'Marvel Entertainment', 'category': ['Comics', 'Superheroes'], 'pages': '128'}, {'title': 'Spider-Man: Anti-Venom', 'author': 'Dan Slott', 'language': None, 'rating': '4', 'publisher': 'Marvel Entertainment', 'category': ['Superheroes'], 'pages': '96'}, {'title': 'Spider-Verse: Volume 1', 'author': 'Dan Slott', 'language': None, 'rating': '4.4', 'publisher': 'Marvel Entertainment', 'category': ['Superheroes'], 'pages': '624'}, {'title': 'Ultimate Spider-Man Vol. 11: Carnage', 'author': 'Brian Michael Bendis', 'language': None, 'rating': '4.1', 'publisher': 'Marvel Entertainment', 'category': ['Comics'], 'pages': '144'}, {'title': 'Venomized', 'author': 'Cullen Bunn', 'language': None, 'rating': '4.5', 'publisher': 'Marvel Entertainment', 'category': ['Comics'], 'pages': '136'}, {'title': 'Permanent Record', 'author': 'Edward Snowden', 'language': None, 'rating': '4.6', 'publisher': 'Metropolitan Books', 'category': ['Legal', 'Biography'], 'pages': '352'}, {'title': 'In Dark Company: A Kate Burkholder Short Story', 'author': 'Linda Castillo', 'language': None, 'rating': '4.3', 'publisher': 'Minotaur Books', 'category': ['Thrillers', 'Fiction'], 'pages': '60'}, {'title': 'Night of the Bold (Kings and Sorcerers Book 6)', 'author': 'Morgan Rice', 'language': None, 'rating': '4.3', 'publisher': 'Morgan Rice', 'category': ['Fiction', 'Fantasy'], 'pages': '250'}, {'title': 'The Weight of Honor (Kings and Sorcerers Book 3)', 'author': 'Morgan Rice', 'language': None, 'rating': '4.4', 'publisher': 'Morgan Rice', 'category': ['Fiction', 'Fantasy'], 'pages': '250'}, {'title': 'Summary: Think and Grow Rich', 'author': 'Nine99 Innovation Lab', 'language': None, 'rating': 'N/A', 'publisher': 'Nine99 Innovation Lab (OPC) Pvt Ltd', 'category': ['Economics', 'Business'], 'pages': '14'}, {'title': 'We', 'author': 'Yevgeny Zamyatin', 'language': None, 'rating': '4.3', 'publisher': 'Pan', 'category': ['Fiction', 'Fantasy'], 'pages': '226'}, {'title': 'Total Control', 'author': 'David Baldacci', 'language': None, 'rating': '4', 'publisher': 'Pan Macmillan', 'category': ['Thrillers', 'Fiction', 'Crime', 'Mystery'], 'pages': '624'}, {'title': 'Twas The Nightshift Before Christmas: Festive hospital diaries from the author of million-copy hit This is Going to Hurt', 'author': 'Adam Kay', 'language': None, 'rating': '4.7', 'publisher': 'Pan Macmillan', 'category': ['Humor'], 'pages': '112'}, {'title': 'Boy Erased: A Memoir', 'author': 'Garrard Conley', 'language': None, 'rating': '4', 'publisher': 'Penguin', 'category': ['Economics', 'Biography'], 'pages': '352'}, {'title': 'Getting Things Done: The Art of Stress-Free Productivity', 'author': 'David Allen', 'language': None, 'rating': '4.5', 'publisher': 'Penguin', 'category': ['Economics'], 'pages': '352'}, {'title': 'No One Is Too Small to Make a Difference', 'author': 'Greta Thunberg', 'language': None, 'rating': '5', 'publisher': 'Penguin', 'category': ['Biography'], 'pages': '112'}, {'title': 'The Infinite Game', 'author': 'Simon Sinek', 'language': None, 'rating': '3.8', 'publisher': 'Penguin', 'category': ['Business'], 'pages': '272'}, {'title': 'The Magic of Thinking Big', 'author': 'David J. Schwartz', 'language': None, 'rating': '4.6', 'publisher': 'Penguin', 'category': ['Economics', 'Business'], 'pages': '256'}, {'title': "Final Option: 'The best one yet'", 'author': 'Clive Cussler', 'language': None, 'rating': '5', 'publisher': 'Penguin UK', 'category': ['Thrillers', 'Fiction', 'Crime', 'Mystery'], 'pages': '400'}, {'title': 'Happy: Why More or Less Everything is Absolutely Fine', 'author': 'Derren Brown', 'language': None, 'rating': '4', 'publisher': 'Random House', 'category': ['Social Science'], 'pages': '576'}, {'title': 'The Power of Habit: Why We Do What We Do in Life and Business', 'author': 'Charles Duhigg', 'language': None, 'rating': '4.1', 'publisher': 'Random House', 'category': ['Economics'], 'pages': '416'}, {'title': 'Financial Statements. Revised and Expanded Edition: A Step-by-Step Guide to Understanding and Creating Financial Reports', 'author': 'Thomas Ittelson', 'language': None, 'rating': '4', 'publisher': 'Red Wheel/Weiser', 'category': ['Economics'], 'pages': '288'}, {'title': 'How To Win Friends and Influence People', 'author': 'Dale Carnegie', 'language': None, 'rating': '4.3', 'publisher': 'Simon and Schuster', 'category': ['Economics', 'Psychology'], 'pages': '320'}, {'title': 'Principles: Life and Work', 'author': 'Ray Dalio', 'language': None, 'rating': '4.7', 'publisher': 'Simon and Schuster', 'category': ['Economics', 'Business'], 'pages': '592'}, {'title': 'Start Day Trading Now: A Quick and Easy Introduction to Making Money While Managing Your Risk', 'author': 'Michael Sincere', 'language': None, 'rating': '5', 'publisher': 'Simon and Schuster', 'category': ['Economics', 'Business'], 'pages': '224'}, {'title': 'The Memoirs of Sherlock Holmes', 'author': 'Arthur Conan Doyle', 'language': None, 'rating': '4.2', 'publisher': 'Simon and Schuster', 'category': ['Fiction', 'Classics', 'Mystery', 'Thrillers', 'Detective'], 'pages': '320'}, {'title': 'Edgedancer: From the Stormlight Archive', 'author': 'Brandon Sanderson', 'language': None, 'rating': '4.8', 'publisher': 'Tor Books', 'category': ['Adventure', 'Fiction'], 'pages': '226'}, {'title': 'Mistborn Trilogy: The Final Empire. The Well of Ascension. The Hero of Ages', 'author': 'Brandon Sanderson', 'language': None, 'rating': '4.7', 'publisher': 'Tor Books', 'category': ['Fantasy'], 'pages': '1712'}, {'title': 'We Should All Be Feminists', 'author': 'Chimamanda Ngozi Adichie', 'language': None, 'rating': '4.2', 'publisher': 'Vintage', 'category': ['Social Science'], 'pages': '32'}, {'title': "The Girl in the Spider's Web: A Lisbeth Salander novel: continuing Stieg Larsson's Millennium Series", 'author': 'David Lagercrantz', 'language': None, 'rating': '4.1', 'publisher': 'Vintage Crime/Black Lizard', 'category': ['Thrillers', 'Fiction', 'Mystery'], 'pages': '416'}, {'title': 'Platform Revolution: How Networked Markets Are Transforming the Economy and How to Make Them Work for You', 'author': 'Geoffrey G. Parker', 'language': None, 'rating': '4.5', 'publisher': 'W. W. Norton & Company', 'category': ['Business'], 'pages': '256'}]
    """


    
    lst = []
    
    for category in dictionary:
        for books in dictionary[category]:
            
            #Searching for duplicate titles
            same_title = False
            for book_info in lst:
                if book_info.get('title') == books.get('title'): 
                    same_title = True

            if not same_title:
                category = set()
                for matching_category in dictionary:
                    for matching_book in dictionary.get(matching_category):
                            if matching_book.get('title') == books.get('title'): 
                                category.add(matching_category) 
                                
                                
                #now formatted properly                      
                lst.append({
                    "title" : books.get('title'),
                    "author" : books.get('author'),
                    "language" : books.get('language '),
                    "rating" : books.get('rating'),
                    "publisher" : books.get('publisher'),
                    "category" : list(category),
                    "pages" : books.get('pages'),
                })       
                
    # Bubble Sort Algorithm 
    
    for i in range(len(lst)):
            for j in range(len(lst) - 1 - i):
                a = lst[j]
                b = lst[j + 1]
                        
                if a["publisher"] > b["publisher"]:
                    lst[j], lst[j+1] = lst[j + 1], lst[j]
                if a["publisher"] == b["publisher"]:
                    if a["title"] > b["title"]:
                        lst[j], lst[j+1] = lst[j + 1], lst[j]
        
    return lst

#Function 3 - sort_books_author - Ben MetCalfe 101234641

def sort_books_author(dictionary : dict) -> list:
    
    empty_lst = []

    for categories in dictionary: #for all the dif categories associted with books
        for books in dictionary[categories]: #for all the books inj those categories
            same_book = False 
            for book_info in empty_lst: #for all the books in the list
                if book_info.get('title') == books.get('title'): #if the book in our list is the same as a book in a category
                    same_book = True #they are the same

            if not same_book: 
                categories = set() 
                for category in dictionary: #for categories in the dict
                    for same_book in dictionary.get(category): #get the categories from the book in our books
                            if same_book.get('title') == books.get('title'): #if they are the same
                                categories.add(category)   #put categories into a set
                empty_lst.append({"title" : books.get('title'),"author" : books.get('author'),"language" : books.get('language '),"rating" : books.get('rating'),"publisher" : books.get('publisher'),"category" : list(categories),"pages" : books.get('pages'),})       #and put categories into formating

    #Bubble Sort Algorithm 
    for i in range(len(empty_lst)):
            for j in range(len(empty_lst) - 1 - i):
                elim1 = empty_lst[j]
                elim2 = empty_lst[j + 1]

                if elim1["author"] > elim2["author"]:
                    empty_lst[j], empty_lst[j+1] = empty_lst[j + 1], empty_lst[j]

    return empty_lst
 
#Function 4 - sort_books_ascending_rate - Chen Chen 101235800

def sort_books_ascending_rate(book_lst: list) -> list:
    
    sort_book = []
    sort_book_combine_category = []
    category_number = 0
    none_rating = []
    
    for lst_category in list(book_lst.values()):
        for lst_category_book in lst_category:
            lst_category_book['category'] = [list(book_lst.keys())[category_number]]
            sort_book.append(lst_category_book)
        category_number += 1
        
    for i in range(len(sort_book)):
        for j in range(len(sort_book)-i-1):
            if sort_book[j].get('title') > sort_book[j+1].get('title'):
                sort_book[j],sort_book[j+1] = sort_book[j+1],sort_book[j]
                
    for i in range(1,len(sort_book)):
        if sort_book[j].get('title') == sort_book[i-1].get('title'):
            sort_book[i]['category'] += sort_book[i-1].get('category')
        else:
            sort_book_combine_category.append(sort_book[i-1])
    sort_book_combine_category.append(sort_book[-1])
    
    for i in range(len(sort_book_combine_category)):
        if sort_book_combine_category[i].get('rating')=='N/A':
            none_rating.append(sort_book_combine_category[i])

    for i in range(len(sort_book_combine_category)):
        for j in range(len(sort_book_combine_category)-i-1):
            a = sort_book_combine_category[j]
            b = sort_book_combine_category[j + 1]
            
            if a['rating']>b['rating']:
                sort_book_combine_category[j], sort_book_combine_category[j + 1] = sort_book_combine_category[j + 1], sort_book_combine_category[j]
            
                                       
    output = none_rating + sort_book_combine_category
                    
    return output

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


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

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


#print(get_books_by_publisher(book_dictionary, 'Marvel Entertainment')) #tester