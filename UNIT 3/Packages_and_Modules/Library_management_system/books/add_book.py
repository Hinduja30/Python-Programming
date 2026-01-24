from ..utilities.logger import logger

def add_book(title, author):
    logger(f"Adding book: {title} by {author}")
    print(f"Book '{title}' by {author} added to the library") 