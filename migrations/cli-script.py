#!/usr/bin/env python
import fire

from artist import Artist, Lable, Song

def name(self):
    return self.name

def art_name(self):
    return self.name

def title(self):
    return self.title


label1=Lable("Republic.Mercury")
artist1=Artist("Post Malone")
song1= Song("Overdrive")


if __name__== '__main__':
    fire.Fire({
      'name':name,
      'art_name':art_name,
      'title':title
  })
