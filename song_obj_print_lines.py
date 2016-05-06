class Song(object):
	def __int__(self, lyrics):
        	self.lyrics = lyrics

	def sing_me_a_song(self):
		for i in self.lyrics:
			print i


happy_bd = Song(["wqwqwwqwqwqwwq,",
		 "sdsdsddsddsds,",
		 "dfdfsdfdfsdfdf!"])

print happy_bd.sing_me_a_song()
