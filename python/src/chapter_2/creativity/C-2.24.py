# ───────────────────────────────────────────────────── Imports ────────────────────────────────────────────────────── #

# Standard Library
from uuid import UUID, uuid4
from enum import Enum
from typing import Union, List, Dict, Literal, Optional
# Third Party Library
from loguru import logger
from pydantic import BaseModel, Field, PrivateAttr, validator

# ───────────────────────────────────────────────────── Code ────────────────────────────────────────────────────────── #

"""
Q: Suppose you are on the design team for a new e-book reader. What are the
primary classes and methods that the Python software for your reader will
need? Your software architecture should at least include ways for customers to 
buy new books, view their list of purchased books, and read their purchased books.

A:

In our system, we will be using validation libraries to speed things up.
We also introduce a TransactionManager to mediate the purchase process so that
customers cannot directly modify the store's inventory or revenue.
"""

# 1. Define a book type and reading status
class BookType(str, Enum):
    """Enumeration of supported book types."""
    PDF = 'pdf'
    EPUB = 'epub'

class BookReadingStatus(BaseModel):
    """Represents the reading status of a book."""
    status: Literal['READING', 'NOT READING'] = Field(default='NOT READING', description='Whether the book is being read.')
    page_num: List[int] = Field(default_factory=list, description='Which pages of the book have been read.')
    num_pages_read: int = Field(0, ge=0, description='The number of pages read of the book.')

# 2. Define a book and search models
class BookSearch(BaseModel):
    """Model to search for a book by title and author."""
    title: str = Field(..., min_length=1, description='The title of the book.')
    author: str = Field(..., min_length=1, description='The author of the book.')

class Book(BookSearch):
    """Represents a book with its metadata and content."""
    id: UUID = Field(default_factory=uuid4, description='Unique book identifier.')
    price: Union[float, int] = Field(..., gt=0, description='The price of the book.')
    num_of_pages: int = Field(..., gt=0, description='The number of pages of the book.')
    content: Dict[int, str] = Field(..., description='The content of each page of the book.')
    type: BookType = Field(..., description='The type of book.')

    def read_page(self, page_num: int) -> str:
        """
        Simulate reading a page of the book.

        Args:
            page_num (int): The page number to read.

        Returns:
            str: The content of the page.
        """
        return self.content.get(page_num, "")

# 3. Define an E-Book (defaulting to EPUB)
class EBook(Book):
    """Represents an E-Book, defaulting its type to EPUB."""
    type: BookType = Field(default=BookType.EPUB, const=True)

# 4. Define an InventoryEntry to manage store inventory
class InventoryEntry(BaseModel):
    """Represents an inventory entry pairing an E-Book with its available count."""
    book: EBook
    count: int = Field(..., ge=0, description='Number of copies available.')

# 5. Define a book store
class EBookStore(BaseModel):
    """Represents an E-Book store with a name, inventory, and revenue."""
    name: str = Field(..., min_length=1, description='The name of the book store.')
    inventory: List[InventoryEntry] = Field(..., description='List of inventory entries for the bookstore.')
    revenue: float = Field(default=0, ge=0, description='Store revenue.')

    # Internal dictionary for quick inventory lookup.
    _inventory_dict: Dict[UUID, InventoryEntry] = PrivateAttr()

    def __init__(self, **data):
        """
        Initializes the EBookStore and creates an internal lookup dictionary for inventory.
        
        Args:
            **data: Keyword arguments corresponding to the model fields.
        """
        super().__init__(**data)
        self._inventory_dict = {entry.book.id: entry for entry in self.inventory}

    def add_book(self, book: EBook, count: int = 1):
        """
        Add copies of an E-Book to the store inventory.

        Args:
            book (EBook): The book to add.
            count (int): Number of copies to add.

        """
        if book.id in self._inventory_dict:
            self._inventory_dict[book.id].count += count
        else:
            entry = InventoryEntry(book=book, count=count)
            self._inventory_dict[book.id] = entry
        self.inventory = list(self._inventory_dict.values())

    def remove_book(self, book_id: UUID, count: int = 1):
        """
        Remove copies of a book from the store inventory.

        Args:
            book_id (UUID): The unique identifier of the book.
            count (int): Number of copies to remove.

        Returns:
            None
        """
        if book_id in self._inventory_dict:
            entry = self._inventory_dict[book_id]
            entry.count -= count
            if entry.count <= 0:
                del self._inventory_dict[book_id]
            self.inventory = list(self._inventory_dict.values())

    @property
    def books(self) -> Dict[UUID, EBook]:
        """
        Get a mapping of book IDs to E-Book objects from the inventory.

        Returns:
            Dict[UUID, EBook]: The books in the store.
        """
        return {book_id: entry.book for book_id, entry in self._inventory_dict.items()}

    @property
    def num_of_books(self) -> Dict[UUID, int]:
        """
        Get a mapping of book IDs to the number of copies available.

        Returns:
            Dict[UUID, int]: The available count for each book.
        """
        return {book_id: entry.count for book_id, entry in self._inventory_dict.items()}

# 6. Define a model for buying a book
class BuyingBook(BookSearch):
    """Represents a customer's intent to buy a book."""
    store: EBookStore = Field(..., description='The store from which the book is being bought.')
    amount: float = Field(..., description='The amount given by the customer to pay for a book.')

# 7. Define a customer
class Customer(BaseModel):
    """Represents a customer with personal details and a record of purchased and reading books."""
    name: str = Field(..., description='Name of customer.')
    dob: str = Field(..., description='Date of birth in the form DD-MM-YYYY.')
    id: UUID = Field(default_factory=uuid4, description='Unique customer identifier.')

    _purchased_books: Dict[UUID, EBook] = PrivateAttr(default_factory=dict)
    _reading_books: Dict[UUID, BookReadingStatus] = PrivateAttr(default_factory=dict)

    @validator('dob')
    def validate_dob(cls, v: str):
        """
        Validate the date of birth format.

        Args:
            v (str): Date of birth as a string.

        Returns:
            str: The validated date string.
        
        Raises:
            ValueError: If the date is not in DD-MM-YYYY format or contains invalid values.
        """
        try:
            day, month, year = v.split('-')
            day, month, year = int(day), int(month), int(year)
        except Exception:
            raise ValueError("Date of birth must be in the form DD-MM-YYYY with numeric values.")
        if not (1 <= day <= 31 and 1 <= month <= 12 and year > 0):
            raise ValueError("Date of birth must be in the form DD-MM-YYYY with valid values.")
        return v

    @property
    def purchased_books(self) -> Dict[UUID, EBook]:
        """
        Get a copy of the customer's purchased books.

        Returns:
            Dict[UUID, EBook]: The purchased books.
        """
        return self._purchased_books.copy()

    @property
    def reading_books(self) -> Dict[UUID, BookReadingStatus]:
        """
        Get a copy of the customer's reading books.

        Returns:
            Dict[UUID, BookReadingStatus]: The reading books.
        """
        return self._reading_books.copy()

    def view_library(self, store: EBookStore) -> List[EBook]:
        """
        View all the E-Books available in the given store.

        Args:
            store (EBookStore): The bookstore to view.

        Returns:
            List[EBook]: List of available E-Books.
        """
        return list(store.books.values())

    def read_book(self, book_search: BookSearch, page_num: int) -> Optional[str]:
        """
        Simulate reading a page of a purchased book.

        Args:
            book_search (BookSearch): Details of the book to read.
            page_num (int): The page number to read.

        Returns:
            Optional[str]: The content of the page if successful; otherwise, None.
        """
        for book_id, book in self._purchased_books.items():
            if book.title == book_search.title and book.author == book_search.author:
                if page_num > max(book.content.keys()):
                    logger.warning("Cannot read a page that does not exist.")
                    return None
                if book_id in self._reading_books:
                    status = self._reading_books[book_id]
                    if page_num not in status.page_num:
                        status.page_num.append(page_num)
                    status.status = 'READING'
                    status.num_pages_read += 1
                else:
                    self._reading_books[book_id] = BookReadingStatus(status='READING', page_num=[page_num], num_pages_read=1)
                return book.read_page(page_num)
        logger.warning("Book has not been purchased.")
        return None

# 8. Introduce a TransactionManager to handle the purchase process
class TransactionManager:
    """Handles transactions between customers and the bookstore, updating store inventory,
    revenue, and customer purchased books without allowing direct manipulation."""
    @classmethod
    def process_purchase(cls, buying_info: BuyingBook, customer: Customer) -> Optional[float]:
        """
        Process the purchase of a book.

        Args:
            buying_info (BuyingBook): The buying request details.
            customer (Customer): The customer attempting the purchase.

        Returns:
            Optional[float]: The change to be returned if the transaction succeeds,
                             or None if the transaction fails.
        """
        matching_entry = None
        for entry in buying_info.store.inventory:
            if entry.book.title == buying_info.title and entry.book.author == buying_info.author:
                matching_entry = entry
                break
        if not matching_entry:
            logger.warning("Book does not exist in store.")
            return None

        book = matching_entry.book
        diff = buying_info.amount - book.price
        if diff < 0:
            logger.warning("Not enough money to purchase book!")
            return None

        # Update the store using its remove_book method.
        buying_info.store.remove_book(book.id, count=1)
        buying_info.store.revenue += book.price

        # Update customer's purchased books.
        if book.id in customer._purchased_books:
            logger.warning("Book has already been purchased!")
        else:
            customer._purchased_books[book.id] = book

        return diff

# ───────────────────────────────────────────────────── Main ────────────────────────────────────────────────────────── #

if __name__ == "__main__":
    logger.info("Storing books in bookstore...")

    # Create some books
    book_1 = EBook(
        title="A",
        author="Mr Man",
        price=10,
        num_of_pages=400,
        content={i: f"Content of page {i}" for i in range(1, 401)}
    )
    book_2 = EBook(
        title="B",
        author="Ms Woman",
        price=5,
        num_of_pages=200,
        content={i: f"Content of page {i}" for i in range(1, 201)}
    )

    # Build the store inventory in a neat, clean way using InventoryEntry.
    inventory = [
        InventoryEntry(book=book_1, count=5),
        InventoryEntry(book=book_2, count=3)
    ]
    book_store = EBookStore(name="BookStore1", inventory=inventory)
    logger.info(f"{book_store.name} has current available books: {[book.id for book in book_store.books.values()]}")
    logger.info(f"{book_store.name} has current revenue: {book_store.revenue}")

    # Add another copy of book_2 to the store.
    logger.info("Adding another copy of book_2...")
    book_store.add_book(book=book_2, count=1)
    logger.info(f"{book_store.name} has current available books: {[book.id for book in book_store.books.values()]}")

    # Create a customer.
    customer_1 = Customer(name="John", dob="19-01-2000")

    # Attempt to purchase with incorrect author (should log a warning).
    TransactionManager.process_purchase(
        buying_info=BuyingBook(store=book_store, title="A", author="Mr Mon", amount=2),
        customer=customer_1
    )

    # Attempt purchase with insufficient funds (should log a warning).
    TransactionManager.process_purchase(
        buying_info=BuyingBook(store=book_store, title="A", author="Mr Man", amount=2),
        customer=customer_1
    )

    # Correct purchase.
    diff = TransactionManager.process_purchase(
        buying_info=BuyingBook(store=book_store, title="A", author="Mr Man", amount=11),
        customer=customer_1
    )
    if diff is not None:
        logger.info(f"Transaction successful. Change returned: {diff}")

    logger.info(f"{book_store.name} has current revenue: {book_store.revenue}")
    logger.info(f"{book_store.name} has current inventory: {book_store.num_of_books}")

    logger.info(f"{customer_1.name} has purchased books: {list(customer_1.purchased_books.keys())}")

    # Customer reads a page of the purchased book.
    reading_book_search = BookSearch(title="A", author="Mr Man")
    page_content = customer_1.read_book(book_search=reading_book_search, page_num=1)
    logger.info(f"{customer_1.name} is reading '{reading_book_search.title}' page 1: {page_content}")
    logger.info(f"{customer_1.name} has current reading inventory: {[(k, v.page_num) for k, v in customer_1.reading_books.items()]}")
