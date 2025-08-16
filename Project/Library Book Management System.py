# class Library:
    
#     def __init__(self):
#         self.books = []
        

#     def add_books(self,name,writer,year):

#         book_info={
#             "title": name,
#             "author": writer,
#             "year"  : year 
#               }
        
#         self.books.append(book_info)
#         # self.name=title
#         # self.writer=author
#         # self.year=year
#         # self.books.append(title)
#         # self.books.append(author)
#         # self.books.append(year)

#     def display_items(self):
#         for book in self.books:
#             print(f"Title : {book['title']} Writer : {book['author']} year : {book['year']}")


#     def Scarch_book(self,book_title):

#         for book in self.books:
#             if book['title'] == book_title:
#                 return book_title
#         print("Books not avlable")
     


# li=Library()
# li.add_books("1984","Gerge orwell",1949)
# li.display_items()
# print(li.Scarch_book('1987'))




class Library:

    def __init__(self):
        self.books = []


    def Add_books(self,name,writer,year):
        book_info = {

            "title": name,
            "author": writer,
            "year"  : year 
         }
        self.books.append(book_info)

    def Display_books(self):
        for book in self.books: 
            print(f"Name: {book['title']} Author: {book['author']} year: {book['year']}")

    
    def Scearch_book(self,book1):

        for book_s in self.books:

            if book_s['title'] == book1:
                print(f"yes {book1} is avlable.")
            else:
                print("Not avlable this book.")
        
        
li=Library()
li.Add_books("Hariporter","jimi",2004)
li.Display_books()
print(li.Scearch_book("Hariporter"))