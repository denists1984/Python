class Game:
    def __init__(self):
        self.current_score = [0, 0]

    def score(self, player):
        a = input("enter 1 or 2 : --->")
        if a == 1:
            self.current_score[0] =+ 1
        elif a == 2:
            self.current_score[1] =+ 1
        else:
            return self.score()
