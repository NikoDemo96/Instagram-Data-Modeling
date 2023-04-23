import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key = True)
    username = Column(String(30), nullable = False, unique = True)
    password = Column(String(30), nullable = False)
    email= Column(String(30), nullable = False, unique = True)

    post = relationship('post') 
    colection = relationship('colection')
    comments = relationship('comments')
    direct_messages = relationship('direct_Messages')


class Post(Base):
    __tablename__ = "post"
    id = Column(Integer, primary_key = True)

    picture = Column(String(30), nullable = False)
    post_description = Column(String(30), nullable = False)
    likes = Column(Integer(15), nullable = False)

    user_id = Column(Integer, ForeignKey('user.id'), nullable = False)
    user = relationship(User)

    comments = relationship('comments')


class Colection(Base):
    __tablename__ = "colection"
    id = Column(Integer, primary_key = True)
    colection_name = Column(String(30), nullable = False)

    post_id = Column(Integer, ForeignKey('planets.id'), nullable = False)
    post = relationship(Post)

    user_id = Column(Integer, ForeignKey('user.id'), nullable = False)
    user = relationship(User)

class Comments(Base):
    __tablename__ = "comments"
    id = Column(Integer, primary_key = True)
    comment_text = Column(String(30), nullable = False)

    post_id = Column(Integer, ForeignKey('planets.id'), nullable = False)
    post = relationship(Post)

    user_id = Column(Integer, ForeignKey('user.id'), nullable = False)
    user = relationship(User)

class Direct_Messages(Base):
    __tablename__ = "direct_messages"
    id = Column(Integer, primary_key = True)
    message_content = Column(String(300), nullable = False)

    post_id = Column(Integer, ForeignKey('planets.id'), nullable = True) #Es True porque un mensaje directo no tiene que tener un post
    post = relationship(Post)

    user_id = Column(Integer, ForeignKey('user.id'), nullable = False) #Es false porque un mensaje directo tiene que tener si o si un destinatario
    user = relationship(User)




    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
