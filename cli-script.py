#!/usr/bin/env python
import fire

from artist import Artist, Lable, Song

class Output(Artist, Lable, Song):

    def name(self, name):
        print("The Label is {name}".format(name=name))

    def art_name(self, art_name):
        return "Artist name is {art_name}".format(art_name=art_name)

    def title(self, title):
        return "The Song title is {title}".format(title=title)


if __name__== '__main__':
    fire.Fire(Output)
