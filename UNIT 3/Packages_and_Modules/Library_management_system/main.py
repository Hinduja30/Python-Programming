import sys
sys.path.append(".")

from books.add_book import add_book
from members.add_member import add_member

add_book("Pride and Prejudice","jane austen")
add_member("Harry","Potter")