from faker import Faker
import random
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import *


fake = Faker()

if __name__ == '__main__':
    
    engine = create_engine('sqlite:///models.db')
    Session = sessionmaker(bind=engine)
    session = Session()

# create record lables
labels =[Label(name='Universal Music'), 
         Label(name='Interscope Records'), 
         Label(name='Atlantic records')]

session.add(labels)
session.commit()

#create label-artists one to many r/ship

for label in labels:
    artists= [Artist(name=fake.name()) for i in range(50)]

session.add(artists)
session.commit()

#many to many r/ship
for artist in artists:
    number_of_songs =random.randint(1,4) #assisgn a random number of songs to each artist

    songs_list =[Song(title=fake.word()) for i in range(82)]

    for a in range(songs_list):
        songs=ArtistSong(artist_id =artist.id)

session.add(songs)
session.commit()

session.close()




# session.close()