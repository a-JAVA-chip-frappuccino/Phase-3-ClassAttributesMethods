import statistics

class Book():

    all = [] # stores list of all objects

    def __init__(self, title, author, page_count):
        self.title = title
        self.author = author
        self.page_count = page_count

        Book.all.append(self) # adds new object to list upon instantiation

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, value):
        if type(value) == str:
            self._title = value
        else:
            raise Exception("Title must be a string!")
        
    def get_author(self):
        return self._author
    
    def set_author(self, new_author):
        if type(new_author) == str:
            self._author = new_author
        else:
            raise Exception("Author must be a string!")
        
    author = property(get_author, set_author)

    @property
    def page_count(self):
        return self._page_count
    
    @page_count.setter
    def page_count(self, new_page_count):
        if type(new_page_count) == int and new_page_count > 0:
        # if isinstance(new_page_count, int) and new_page_count > 0:
            self._page_count = new_page_count
        else:
            raise Exception("Page count must be a positive integer!")
        
    def get_all_books():
        return Book.all
    
    @classmethod
    def get_first_book(cls):
        return cls.all[0]
    
    def get_avg_page_count():
        '''
            get each book object in list and get page count of each,
            summing those page counts up and dividing by the number of objects.
            or performing artihmetic mean directly on list of page counts.
        '''

        '''
        sum_page_count = 0

        for book in Book.all:
            page_count = book.page_count

            sum_page_count += page_count # sum_page_count = sum_page_count + page_count

        avg_page_count = sum_page_count / len(Book.all)

        return avg_page_count
        '''

        '''
        all_page_counts = [book.page_count for book in Book.all]

        return sum(all_page_counts) / len(all_page_counts)
        '''

        all_page_counts = [book.page_count for book in Book.all]

        return statistics.mean(all_page_counts)
    
    @classmethod
    def get_longest_book(cls):
        '''
            get each book object in list and get page count of each,
            storing book and object as current maximums if larger that previous current maximum.
            or store books associated with page counts and calculate maximum of latter.
        '''
        
        '''
        curr_longest_book = None
        curr_longest_count = 0

        for book in cls.all:
            if book.page_count > curr_longest_count:
                curr_longest_count = book.page_count
                curr_longest_book = book

        return curr_longest_book
        '''

        freq_dict = {}

        for book in cls.all:
            freq_dict[book] = book.page_count

        # freq_dict = {book : book.page_count for book in cls.all}

        # return max(freq_dict, key = lambda key : freq_dict[key])
        return max(freq_dict, key = freq_dict.get)
    
    def __str__(self):
        return f"Title: {self.title} and Page Count: {self.page_count}"
    
    def __repr__(self):
        return f"Title: '{self.title}' and Page Count: {self.page_count}"
        
'''
    SANDBOX ENVIRONMENT
'''

twilight = Book("Twilight", "Stephanie Meyer", 200)
new_moon = Book("New Moon", "Stephanie Meyer", 400)
eclipse = Book("Eclipse", "Stephanie Meyer", 375)
breaking_dawn = Book("Breaking Dawn", "Stephanie Meyer", 310)
bree_tanner = Book("The Short Second Life of Bree Tanner", "Stephanie Meyer", 100)
midnight_sun = Book("Midnight Sun", "Stephanie Meyer", 140)

print(f"The average of all the page counts: {Book.get_avg_page_count()}")
print(f"The longest book is {Book.get_longest_book().title} and it has a length of {Book.get_longest_book().page_count} pages.")