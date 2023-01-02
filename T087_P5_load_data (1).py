#Zarif Khan 101224172
#Aiden Hepburn 101220580
#Chen Chen 101235800
#Ben MetCalfe 101234641

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



    
    
    
    
    

