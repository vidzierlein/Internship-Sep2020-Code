'''Define a class called Songs, it will show the lyrics of a song. 
Its __init__() method should have 
two arguments:selfanf lyrics.lyricsis a list. 
Inside your class create a method called sing_me_a_song
that prints each element of lyricson his own line. 
Define a varible:

happy_bday = Song(["May god bless you, ",
                   "Have a sunshine on you,",
                   "Happy Birthday to you !"])
Call the sing_me_songmehod on this variable.

1. define class Songs - "This class shows the lyrics of the song"
2. __init__ method has 2 arguments (self, lyrics)
3. define sing_me_a_song method - this prints each element 
of lyrics on its own line.
4. define an obejct variable.
5. call the sing_me_a_song method for this variable object'''

class Songs:
    "displays the lyrics of the song"
    def __init__(self, lyrics):
        "Initializing arguments self and lyrics"
        self.lyrics = lyrics

    def sing_me_a_song(self):
        "print each element of the lyrics on its own line"
        for each_lyric in self.lyrics:
            print(each_lyric)

song_birthday = Songs(["May god bless you,",
                        "Have a sunshine on you,",
                        "Happy Birthday to you !"])
song_birthday.sing_me_a_song()

    