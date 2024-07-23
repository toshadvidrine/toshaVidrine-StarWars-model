import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, Text, Table
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

# Association table for User favorites
favorites = Table('favorites', Base.metadata,
    Column('user_id', Integer, ForeignKey('user.id'), primary_key=True),
    Column('person_id', Integer, ForeignKey('person.id'), nullable=True),
    Column('planet_id', Integer, ForeignKey('planet.id'), nullable=True),
    Column('starship_id', Integer, ForeignKey('starship.id'), nullable=True)
)

class User(Base):
    __tablename__ = 'user'
    
    id = Column(Integer, primary_key=True)
    username = Column(String(80), unique=True, nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    password = Column(String(200), nullable=False)
    favorites = relationship('Favorite', backref='user', lazy=True)

    def __repr__(self):
        return f'<User {self.username}>'

class Person(Base):
    __tablename__ = 'person'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    height = Column(String(10))
    mass = Column(String(10))
    hair_color = Column(String(50))
    skin_color = Column(String(50))
    eye_color = Column(String(50))
    birth_year = Column(String(10))
    gender = Column(String(10))
    homeworld = Column(String(100))
    image_url = Column(String(200))  # For card display
    description = Column(Text)  # For detailed view
    is_favorite = Column(Boolean, default=False)  # For favorite functionality

    def __repr__(self):
        return f'<Person {self.name}>'

class Planet(Base):
    __tablename__ = 'planet'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    diameter = Column(String(20))
    climate = Column(String(50))
    gravity = Column(String(50))
    terrain = Column(String(100))
    surface_water = Column(String(10))
    population = Column(String(20))
    image_url = Column(String(200))  # For card display
    description = Column(Text)  # For detailed view
    is_favorite = Column(Boolean, default=False)  # For favorite functionality

    def __repr__(self):
        return f'<Planet {self.name}>'

class Starship(Base):
    __tablename__ = 'starship'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    model = Column(String(100))
    manufacturer = Column(String(100))
    cost_in_credits = Column(String(20))
    length = Column(String(20))
    max_atmosphering_speed = Column(String(20))
    crew = Column(String(10))
    passengers = Column(String(10))
    cargo_capacity = Column(String(20))
    consumables = Column(String(50))
    hyperdrive_rating = Column(String(10))
    starship_class = Column(String(50))
    image_url = Column(String(200))  # For card display
    description = Column(Text)  # For detailed view
    is_favorite = Column(Boolean, default=False)  # For favorite functionality

    def __repr__(self):
        return f'<Starship {self.name}>'

class Favorite(Base):
    __tablename__ = 'favorite'
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    person_id = Column(Integer, ForeignKey('person.id'), nullable=True)
    planet_id = Column(Integer, ForeignKey('planet.id'), nullable=True)
    starship_id = Column(Integer, ForeignKey('starship.id'), nullable=True)

    def __repr__(self):
        return f'<Favorite User: {self.user_id}, Person: {self.person_id}, Planet: {self.planet_id}, Starship: {self.starship_id}>'

# Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
