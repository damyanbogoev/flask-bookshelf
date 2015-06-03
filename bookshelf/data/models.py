from flask.ext.sqlalchemy import SQLAlchemy

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
