__author__ = 'josh@thecrazypenguin.com'

from flask.ext.sqlalchemy import SQLAlchemy

db = SQLAlchemy()

BookPublisher = db.Table('BookPublisher',
                      db.Column('id', db.Integer, primary_key=True),
                      db.Column('bookId', db.Integer, db.ForeignKey('Book.id')),
                      db.Column('publisherId', db.Integer, db.ForeignKey('Publisher.id')))
BookSystem = db.Table('BookSystem',
                   db.Column('id', db.Integer, primary_key=True),
                   db.Column('bookId', db.Integer, db.ForeignKey('Book.id')),
                   db.Column('systemId', db.Integer, db.ForeignKey('System.id')))
BookTag = db.Table('BookTag',
                db.Column('id', db.Integer),
                db.Column('bookId', db.Integer, db.ForeignKey('Book.id')),
                db.Column('tagId', db.Integer, db.ForeignKey('Tag.id')))


class Base(db.Model):
    __abstract__ = True
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
                              onupdate=db.func.current_timestamp())


class Library(Base):
    __tablename__ = "Library"

    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String)
    shelves = db.relationship("Shelf", backref="library")

    def __repr__(self):
        return "Library: {}".format(self.name)


class Shelf(Base):
    __tablename__ = "Shelf"

    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String)
    library_id = db.Column(db.Integer, db.ForeignKey('Library.id'))

    books = db.relationship("Book", backref="shelf")

    def __repr__(self):
        return "Shelf: {}".format(self.name)


class Book(Base):
    __tablename__ = "Book"

    name = db.Column(db.String, nullable=False)
    is_physical = db.Column(db.Boolean, default=False)
    pages = db.Column(db.Integer, nullable=False, default=0)
    cover = db.Column(db.BLOB)
    rating = db.Column(db.Integer, nullable=False, default="0")
    shelf_id = db.Column(db.Integer, db.ForeignKey('Shelf.id'))

    publishers = db.relationship("Publisher", secondary=BookPublisher, backref='books')
    systems = db.relationship("System", secondary=BookSystem, backref='books')
    tags = db.relationship("Tag", secondary=BookTag, backref='books')

    def __repr__(self):
        if self.is_physical:
            return "Book: {}".format(self.name)
        else:
            return "EBook: {}".format(self.name)


class Publisher(Base):
    __tablename__ = "Publisher"
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String)
    #books = db.relationship("Book", secondary=BookPublisher, backref="publishers")


class System(Base):
    __tablename__ = "System"
    name = db.Column(db.String, nullable=False)
    #books = db.relationship("Book", secondary=BookSystem, backref="systems")


class Tag(Base):
    __tablename__ = "Tag"
    name = db.Column(db.String, nullable=False)
    #books = db.relationship("Book", secondary=BookTag, backref="tags")
