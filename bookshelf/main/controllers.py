from flask import Blueprint, render_template, current_app
from bookshelf.cache import cache
from bookshelf.data.models import Author, Book


main = Blueprint('main', __name__, template_folder='templates')


@main.route('/')
@cache.cached(300, key_prefix='main_index')
def index():
    return render_template("index.htm")


@main.route('books/')
@cache.cached(300, key_prefix='display_books')
def display_books():
    books = [book for book in Book.query.all()]
    current_app.logger.info('Displaying all books.')

    return render_template("books.htm", books=books)


@main.route('authors/')
@cache.cached(300, key_prefix='display_authors')
def display_authors():
    authors = [author for author in Author.query.all()]
    current_app.logger.info('Displaying all authors.')

    return render_template("authors.htm", authors=authors)
