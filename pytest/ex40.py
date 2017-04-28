class Song(object):
	def __init__(self,lyrics):
		self.lyrics = lyrics
	def sing_me_a_song(self):
		for line in self.lyrics:
			print( line)

happy_bday = Song([" if taking you back to my north home",
			" let us to remember the past time",
			" maybe you will love my home",
			" and the north of the wind"])

bulls_on_parade = Song([" you and me as the same kind",
			" the longly ghost",
			" in the north of the earth"])
happy_bday.sing_me_a_song()
bulls_on_parade.sing_me_a_song()
