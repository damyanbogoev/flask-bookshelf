from flask_security.utils import encrypt_password
from bookshelf.data.models import db, Author, Book
from bookshelf import app


def create_authors_and_books(ctx):
    author1 = Author("Ivan Vazov")
    author2 = Author("Hristo Botev")

    book1 = Book("Epic of the Forgotten", author1, "15705091.jpg", 5)
    book2 = Book("The Poems of Hristo Botev", author2, "20911420.jpg", 5)

    ctx.session.add(author1)
    ctx.session.add(author2)
    ctx.session.add(book1)
    ctx.session.add(book2)

    ctx.session.commit()


def create_roles(ctx):
    ctx.create_role(name="admin")
    ctx.commit()


def create_users(ctx):
    users = [
        ("admin@test.com", "admin", "1234", ["admin"], True),
        ("user@test.com", "user", "6789", [], True),
    ]
    for user in users:
        email = user[0]
        username = user[1]
        password = user[2]
        is_active = user[4]
        if password is not None:
            password = encrypt_password(password)
        roles = [ctx.find_or_create_role(rn) for rn in user[3]]
        ctx.commit()
        user = ctx.create_user(email=email, password=password, active=is_active)
        ctx.commit()
        for role in roles:
            ctx.add_role_to_user(user, role)
        ctx.commit()


data_store = app.security.datastore
with app.app_context():
    db.drop_all()
    db.create_all()

    create_authors_and_books(db)
    create_roles(data_store)
    create_users(data_store)
