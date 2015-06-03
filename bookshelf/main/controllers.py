from flask import Blueprint, render_template
from bookshelf.data.models import Book


main = Blueprint('main', __name__, template_folder='templates')


@main.route('/')
def index():
    return render_template("index.htm")


@main.route('books/')
def display_books():
    books = [book for book in Book.query.all()]

    return render_template("books.htm", books=books)
