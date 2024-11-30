class Document:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display_info(self):
        print("Title:", self.title)
        print("Author:", self.author)

class Book(Document):
    def __init__(self, title, author, genre=None, pages=None):
        super().__init__(title, author)
        self.genre = genre
        self.pages = pages

    def display_info(self):
        super().display_info()
        if self.genre:
            print("Genre:", self.genre)
        if self.pages:
            print("Pages:", self.pages)

class Article(Document):
    def __init__(self, title, author, journal=None, doi=None):
        super().__init__(title, author)
        self.journal = journal
        self.doi = doi

    def display_info(self):
        super().display_info()
        if self.journal:
            print("Journal:", self.journal)
        if self.doi:
            print("DOI:", self.doi)

def save_documents_to_file(file_name, documents, is_book=True):
    with open(file_name, "w") as file:
        for document in documents:
            if is_book:
                file.write(f"{document.title},{document.author},{document.genre if document.genre else ''},{document.pages if document.pages else ''}\n")
            else:
                file.write(f"{document.title},{document.author},{document.journal if document.journal else ''},{document.doi if document.doi else ''}\n")

def read_documents_from_file(file_name, is_book=True):
    documents = []
    try:
        with open(file_name, "r") as file:
            for line in file:
                data = line.strip().split(",")
                if is_book:
                    title, author, genre, pages = data[0], data[1], data[2] or None, int(data[3]) if data[3] else None
                    documents.append(Book(title, author, genre, pages))
                else:
                    title, author, journal, doi = data[0], data[1], data[2] or None, data[3] or None
                    documents.append(Article(title, author, journal, doi))
    except FileNotFoundError:
        print("No documents found.")
    return documents

books = read_documents_from_file("books.txt", True)
articles = read_documents_from_file("articles.txt", False)

while True:
    print("\nMenu:")
    print("1. Add Book")
    print("2. Add Article")
    print("3. Display Books")
    print("4. Display Articles")
    print("5. Save and Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        title = input("Enter title: ")
        author = input("Enter author: ")
        genre = input("Enter genre (or leave blank): ")
        pages = input("Enter number of pages (or leave blank): ")
        books.append(Book(title, author, genre, int(pages) if pages else None))
        print("Book added successfully!")
    elif choice == "2":
        title = input("Enter title: ")
        author = input("Enter author: ")
        journal = input("Enter journal (or leave blank): ")
        doi = input("Enter DOI (or leave blank): ")
        articles.append(Article(title, author, journal, doi))
        print("Article added successfully!")
    elif choice == "3":
        for book in books:
            book.display_info()
            print()
    elif choice == "4":
        for article in articles:
            article.display_info()
            print()
    elif choice == "5":
        save_documents_to_file("books.txt", books, True)
        save_documents_to_file("articles.txt", articles, False)
        print("Data saved. Exiting program.")
        break
    else:
        print("Invalid choice. Please try again.")