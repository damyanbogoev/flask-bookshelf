from flask import Blueprint, render_template
from bookshelf.data.models import Author, Book


main = Blueprint('main', __name__, template_folder='templates')


@main.route('/')
def index():
    return render_template("index.htm")


@main.route('books/')
def display_books():
    books = [book for book in Book.query.all()]

    return render_template("books.htm", books=books)


@main.route('authors/')
def display_authors():
    authors = [author for author in Author.query.all()]

    return render_template("authors.htm", authors=authors)
