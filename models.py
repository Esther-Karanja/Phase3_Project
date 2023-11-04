from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
from artist import *

Base =declarative_base()

class Label(Base):
     __tablename__='labels'

     id =Column(Integer(), primary_key =True)
     name =Column(String(), nullable= False)
     artist=relationship('Artist', backref='owner')  #one to many relationship with Artist "has"

     def __repr__(self):
         return f"{self.id} {self.name}"

class Artist(Base):
     __tablename__='artists'

     id =Column(Integer(), primary_key =True)
     name =Column(String(), nullable= False)
     label_id =Column(Integer(), ForeignKey('labels.id')) #one to many relationship with Label "belongs to"

     def __repr__(self):
         return f"{self.id} {self.name}"
 
     
class Song(Base):
     __tablename__='songs'

     id =Column(Integer(), primary_key =True)
     title =Column(String(), nullable= False)

     def __repr__(self):
         return f"{self.id} {self.title}"

 #many-to-many relationship between artists and songs    
class ArtistSong(Base):
     __tablename__='artist_songs'

     id=Column(Integer(), primary_key =True)
     artist_id =Column(Integer(), ForeignKey('artists.id'))
     song_id=Column(Integer(), ForeignKey('songs.id'))

     artist=relationship('Artist', back_populates='artist_songs')
     song=relationship('Song', back_populates='artist_songs')

     def __repr__(self):
        return f'artist_id={self.artist_id}, ' + \
            f'song_id={self.song_id})'