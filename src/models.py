import os
import sys
from sqlalchemy.orm import declarative_base, Mapped, mapped_column
from sqlalchemy import create_engine, ForeignKey
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    email:Mapped[str] = mapped_column(nullable=False)
    profile_pic: Mapped[str] = mapped_column(nullable=True)

class Post(Base):
    __tablename__ = 'post'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id: Mapped[int] = mapped_column(primary_key=True)
    caption: Mapped[str]
    media: Mapped[str]
    user_id: Mapped[int]= mapped_column(ForeignKey("user.id"))
    time_stamp: Mapped[str] = mapped_column(nullable=False)


class About(Base):
     __tablename__ = 'about'
     id: Mapped[int] = mapped_column(primary_key=True)
     user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
     date_of_birth: Mapped[str] 
     gender: Mapped[str] = mapped_column(nullable = False)
     address: Mapped[str]

class Media(Base):
    __tablename__= 'media'
    id: Mapped[int] = mapped_column(primary_key = True)
    post_id: Mapped[int] = mapped_column(ForeignKey("post.id"))
    url: Mapped[str]= mapped_column()
    
   

def to_dict(self):
    return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
