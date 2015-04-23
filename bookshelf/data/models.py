from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from bookshelf.data.database import Base


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    email = Column(String(120), unique=True)

    def __init__(self, name=None, email=None):
        self.name = name
        self.email = email

    def __repr__(self):
        return '<User %r>' % (self.name)


class Author(Base):
    __tablename__ = 'authors'
    id = Column(Integer, primary_key=True)
    names = Column(String(100), unique=True)
    books = relationship('Book', backref='author', lazy='dynamic')

    def __init__(self, names):
        self.names = names

    def __repr__(self):
        return '<Author %r>' % (self.names)


class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    title = Column(String(80))
    rating = Column(Integer)
    image = Column(String(30))
    author_id = Column(Integer, ForeignKey('authors.id'))

    def __init__(self, title, author_id, image, rating=0):
        self.title = title
        self.author_id = author_id
        self.image = image
        self.rating = rating

    def __repr__(self):
        return '<Book %r>' % (self.title)
