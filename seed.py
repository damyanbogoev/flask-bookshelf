from bookshelf import app
from bookshelf.data.models import db, Author, Book

with app.app_context():
    db.drop_all()
    db.create_all()

    author1 = Author('Ivan Vazov')
    author2 = Author('Hristo Botev')

    book1 = Book('Epic of the Forgotten', author1, '15705091.jpg', 5)
    book2 = Book('The Poems of Hristo Botev', author2, '20911420.jpg', 5)

    db.session.add(author1)
    db.session.add(author2)
    db.session.add(book1)
    db.session.add(book2)

    db.session.commit()
