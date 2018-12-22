class Song(object):
    def __init__(self, lyrics):
        self.lyrics = lyrics
    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

happy_bday = Song(["Happy birthday to you",
                   "I do not want to get sued",
                   "So I will stop right there"])

bulls_on_parde = Song(["They rally around the family",
                        "With pockets full of shells"])
happy_bday.sing_me_a_song()
bulls_on_parde.sing_me_a_song()
