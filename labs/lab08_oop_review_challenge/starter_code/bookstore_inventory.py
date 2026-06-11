# Lab 8: Object-Oriented Programming Review Challenge

from book import Book


def create_inventory(filename):
    """
    Read books from csv file, create and return a list of Book objects.
    """
    books = []
    with open(filename, "r") as f:
        for line in f:
            list1 = line.split(",")
            if list1[0] == "title":
                continue
            else:
                books.append(Book(list1[0], list1[1], list1[2], list1[3], list1[4], list1[5]))
    return books


def print_inventory(books):
    """
    Print every book in the inventory.
    """
    for book in books:
        print(book)


def total_inventory(books):
    """
    Return the total number of all books in inventory.
    """
    return len(books)


def find_by_author(books, author):
    """
    Return a list of books written by the specified author.
    """
    author_books = []
    for book in books:
        if book.author == author:
            author_books.append(book)
    return author_books


def find_low_stock(books, threshold):
    """
    Return a list of books whose quantity is less than or equal to threshold.
    """
    low_stock = []
    for book in books:
        if book.amount <= threshold:
            low_stock.append(book)
    return low_stock


def print_books(books):
    """
    Print a list of books.
    """
    for book in books:
        print(book)


def main():
    inventory = create_inventory("../data/booklist.csv")

    print("Full Inventory")
    print("--------------")
    print_inventory(inventory)

    print()
    print("Total inventory:", total_inventory(inventory))

    print()
    print("Books by Octavia Butler")
    print("-----------------------")
    print_books(find_by_author(inventory, "Octavia Butler"))

    print()
    print("Low Stock Books")
    print("---------------")
    print_books(find_low_stock(inventory, 3))

    print()
    print("Sorted by Title")
    print("---------------")
    sorted_books = sorted(inventory)
    print_books(sorted_books)


main()
