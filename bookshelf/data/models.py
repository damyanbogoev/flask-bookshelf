from flask_sqlalchemy import SQLAlchemy
from flask_security import UserMixin, RoleMixin

db = SQLAlchemy()


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    rating = db.Column(db.Integer)
    image = db.Column(db.String(30))
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'))
    author = db.relationship('Author',
                             backref=db.backref('books', lazy='joined'))

    def __init__(self, title, author, image=None, rating=0):
        self.title = title
        self.author = author
        self.image = image
        self.rating = rating

    def __repr__(self):
        return '<Book %r>' % (self.title)


class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    names = db.Column(db.String(100), unique=True)

    def __init__(self, names):
        self.names = names

    def __repr__(self):
        return '<Author %r>' % (self.names)


roles_users = db.Table('roles_users', \
db.Column('user_id', db.Integer(), db.ForeignKey('user.id')), \
db.Column('role_id', db.Integer(), db.ForeignKey('role.id')))


class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Role %r>' % (self.name)


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean())
    roles = db.relationship('Role', secondary=roles_users,
                            backref=db.backref('users', lazy='dynamic'))

    def __init__(self, email, password, active, roles):
        self.email = email
        self.password = password
        self.active = active
        self.roles = roles

    def __repr__(self):
        return '<User %r>' % (self.email)
