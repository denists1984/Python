def __str__(self):
    return '{} {}, XP: {}, HP: {}'.format(self.color.title(),
                                          self.__class__.__name__,
                                          self.expiareance)

from game import Game



class GameScore(Game):
    def __str__(self):
        return 'Player 1: {}; Player 2: {}'.format(self.score[0], self.score[1])
    pass
