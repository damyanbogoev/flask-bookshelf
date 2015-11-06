from bookshelf import app
from bookshelf.data.models import db, Author, Book, Role, User

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

    role1 = Role('admin')
    role2 = Role('editor')
    role3 = Role('reader')
    db.session.add(role1)
    db.session.add(role2)
    db.session.add(role3)

    user1 = User('admin', '1234', True)
    user2 = User('editor', '2345', True)
    db.session.add(user1)
    db.session.add(user2)

    db.session.commit()
