from flask import Blueprint, render_template


main = Blueprint('main', __name__, template_folder='templates')


@main.route('/')
def index():
    return render_template("index.htm")


@main.route('books/')
def display_books():
    books = {
        "Learn Python The Hard Way": {
            "author": "Shaw, Zed",
            "rating": "3.92",
            "image": "ef0ceaab-32a8-47fb-ba13-c0b362d970da.jpg"
        },
        "House of Cards": {
            "author": "Dobbs, Michael",
            "rating": "3.92",
            "image": "e9bf34c2-d1f7-4aef-99d8-846f6ca2404d.jpg"
        },
        "Pro Puppet": {
            "author": "Krum, Spencer",
            "rating": "3.75",
            "image": "702ec908-9d87-49fe-80a6-ef0bc6a95ee7.jpg",
            "hidden": True
        }
    }

    return render_template("books.htm", books=books)
