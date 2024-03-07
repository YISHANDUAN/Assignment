class Vinyl:
    def __init__(self, album, artist, year):
        self.album = album
        self.artist = artist
        self.year = year

    def display(self):
        print(self.album + ',' + self.artist +',' + self.year)

def run01():
    R= Vinyl('R', 'Rosé', '2021')
    R.display()

