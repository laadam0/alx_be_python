from book_class import Book

def main():
    my_book = Book("1984", "George Orwell", 1949)

    print(my_book)            # Should use __str__
    print(repr(my_book))      # Should use __repr__

    del my_book               # Should trigger __del__

if __name__ == "__main__":
    main()
