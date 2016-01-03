from flask import Blueprint, current_app, render_template
from bookshelf.cache import cache
from bookshelf.data.models import Author, Book


main = Blueprint('main', __name__, template_folder='templates')

@main.route('/books/')
@cache.cached(300)
def display_books():
    books = [book for book in Book.query.all()]
    current_app.logger.info('Displaying all books.')

    return render_template("books.htm", books=books)

@main.route('/authors/')
@cache.cached(300)
def display_authors():
    authors = [author for author in Author.query.all()]
    current_app.logger.info('Displaying all authors.')

    return render_template("authors.htm", authors=authors)
