from book_class import Book

if __name__ == "__main__":
    # Create some book objects
    book1 = Book("Things Fall Apart", "Chinua Achebe", 1958)
    book2 = Book("Purple Hibiscus", "Chimamanda Ngozi Adichie", 2003)

    # Print with __str__
    print(book1)
    print(book2)

    # Print with __repr__
    print(repr(book1))
    print(repr(book2))
