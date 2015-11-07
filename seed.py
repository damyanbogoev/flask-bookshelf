from bookshelf import app
from bookshelf.data.models import db, Author, Book
from flask_security.utils import encrypt_password

def create_authors_and_books(db):
    author1 = Author('Ivan Vazov')
    author2 = Author('Hristo Botev')

    book1 = Book('Epic of the Forgotten', author1, '15705091.jpg', 5)
    book2 = Book('The Poems of Hristo Botev', author2, '20911420.jpg', 5)

    db.session.add(author1)
    db.session.add(author2)
    db.session.add(book1)
    db.session.add(book2)

    db.session.commit()

def create_roles(data_store):
    data_store.create_role(name='admin')
    data_store.commit()

def create_users(data_store):
    users = [('admin@test.com', 'admin', '1234', ['admin'], True), \
    ('user@test.com', 'user', '6789', [], True)]
    for user in users:
        email = user[0]
        username = user[1]
        password = user[2]
        is_active = user[4]
        if password is not None:
            password = encrypt_password(password)
        roles = [data_store.find_or_create_role(rn) for rn in user[3]]
        data_store.commit()
        user = data_store.create_user(email=email, password=password, active=is_active)
        data_store.commit()
        for role in roles:
            data_store.add_role_to_user(user, role)
        data_store.commit()

data_store = app.security.datastore
with app.app_context():
    db.drop_all()
    db.create_all()

    create_authors_and_books(db)
    create_roles(data_store)
    create_users(data_store)
